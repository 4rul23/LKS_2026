from flask import Flask, request, render_template, redirect, url_for, session, make_response
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

FLAG = "STELKCSC{p4r4m3t3r_p0llut10n_tw1n_1d3nt1ty}"

# Candidates Database (Paslon)
CANDIDATES = {
    '01': {'name': 'H. Anies Rasyid Baswedan - H. Muhaimin Iskandar', 'party': 'Koalisi Perubahan', 'role': 'Paslon 01', 'votes': 145032, 'image': 'anis.png'},
    '02': {'name': 'H. Prabowo Subianto - Gibran Rakabuming Raka', 'party': 'Koalisi Indonesia Maju', 'role': 'Paslon 02', 'votes': 178921, 'image': 'prabowo.png'},
    '03': {'name': 'H. Ganjar Pranowo - Prof. Dr. Mahfud MD', 'party': 'PDIP & Koalisi', 'role': 'Paslon 03', 'votes': 98453, 'image': 'ganjar.png'},
}

# Admin Override (Ketua KPU)
# Only this NIK can view the "Verified" flag in the receipt
NIK_KETUA_KPU = '9999000011112222' 

# Current Logged in Voter (Simulated Session)
# Normal citizen NIK
CURRENT_NIK = '3174052001950005' 

@app.route('/')
def index():
    return render_template('index.html', 
                         candidates=CANDIDATES, 
                         current_nik=CURRENT_NIK)

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'GET':
        candidate_id = request.args.get('candidate', '')
        voter_id = request.args.get('voter_id', CURRENT_NIK)
        
        if candidate_id not in CANDIDATES:
            return redirect(url_for('index'))
            
        return render_template('vote.html',
                             candidate=CANDIDATES[candidate_id],
                             candidate_id=candidate_id,
                             voter_id=voter_id,
                             current_nik=CURRENT_NIK)
    
    # POST - Process vote
    if request.method == 'POST':
        # Get all voter_id values (for HPP vulnerability)
        voter_ids = request.form.getlist('voter_id')
        candidate_id = request.form.get('candidate_id', '')
        
        # SECURITY CHECK: Validate first voter_id parameter
        # (Simulates Firewall filtering first param ONLY)
        first_voter_id = voter_ids[0] if voter_ids else ''
        
        if first_voter_id != CURRENT_NIK:
            return render_template('error.html', 
                                 message="Peringatan Keamanan: NIK tidak cocok dengan sesi login. Anda hanya dapat memilih atas nama sendiri.",
                                 current_nik=CURRENT_NIK)
        
        # BACKEND PROCESSING: Uses LAST voter_id (The Vulnerability)
        # Python/Flask getlist allows seeing all, but if we naively took the last one...
        # Here we simulate the logic: "Trust the last parameter as the definitive one"
        actual_voter_id = voter_ids[-1] if voter_ids else first_voter_id
        
        # Check if voting as Ketua KPU
        is_admin_vote = (actual_voter_id == NIK_KETUA_KPU)
        
        if candidate_id in CANDIDATES:
            # Admin vote weights more (Simulation of "Super User" testing)
            CANDIDATES[candidate_id]['votes'] += (1000 if is_admin_vote else 1)
        
        return render_template('success.html',
                             candidate=CANDIDATES.get(candidate_id, {}),
                             candidate_id=candidate_id,
                             voter_id=actual_voter_id,
                             is_admin=is_admin_vote,
                             flag=FLAG if is_admin_vote else None,
                             current_nik=CURRENT_NIK)

@app.route('/leaderboard')
def leaderboard():
    sorted_candidates = sorted(
        [(k, v) for k, v in CANDIDATES.items()],
        key=lambda x: x[1]['votes'],
        reverse=True
    )
    return render_template('leaderboard.html',
                         candidates=sorted_candidates,
                         current_nik=CURRENT_NIK)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5008)
