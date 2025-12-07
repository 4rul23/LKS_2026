from flask import Flask, request, render_template, redirect, url_for, session, make_response
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

FLAG = "STELKCSC{p4r4m3t3r_p0llut10n_tw1n_1d3nt1ty}"

# Employee database
EMPLOYEES = {
    'E001': {'name': 'Budi Santoso', 'role': 'Staff', 'department': 'Engineering', 'votes': 12},
    'E002': {'name': 'Dewi Lestari', 'role': 'Staff', 'department': 'Marketing', 'votes': 8},
    'E003': {'name': 'Ahmad Wijaya', 'role': 'Staff', 'department': 'Finance', 'votes': 15},
    'E999': {'name': 'Director Account', 'role': 'Director', 'department': 'Executive', 'votes': 0},
}

# Current logged in user (simulated)
CURRENT_USER = 'E001'  # Budi

@app.route('/')
def index():
    return render_template('index.html', 
                         employees=EMPLOYEES, 
                         current_user=CURRENT_USER,
                         current_employee=EMPLOYEES[CURRENT_USER])

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'GET':
        candidate = request.args.get('candidate', '')
        voter_id = request.args.get('voter_id', CURRENT_USER)
        
        if candidate not in EMPLOYEES:
            return redirect(url_for('index'))
            
        return render_template('vote.html',
                             candidate=EMPLOYEES[candidate],
                             candidate_id=candidate,
                             voter_id=voter_id,
                             current_employee=EMPLOYEES[CURRENT_USER])
    
    # POST - Process vote
    if request.method == 'POST':
        # Get all voter_id values (for HPP vulnerability)
        voter_ids = request.form.getlist('voter_id')
        candidate_id = request.form.get('candidate_id', '')
        
        # SECURITY CHECK: Validate first voter_id parameter
        # (This simulates a WAF or security middleware that only checks first param)
        first_voter_id = voter_ids[0] if voter_ids else ''
        
        if first_voter_id != CURRENT_USER:
            return render_template('error.html', 
                                 message="Security Alert: Voter ID mismatch. You can only vote as yourself.",
                                 current_employee=EMPLOYEES[CURRENT_USER])
        
        # BACKEND PROCESSING: Uses LAST voter_id (vulnerability!)
        # Many frameworks overwrite with last value or use last in list
        actual_voter_id = voter_ids[-1] if voter_ids else first_voter_id
        
        # Check if voting as Director (E999)
        is_director_vote = (actual_voter_id == 'E999')
        
        if candidate_id in EMPLOYEES:
            EMPLOYEES[candidate_id]['votes'] += (10 if is_director_vote else 1)
        
        return render_template('success.html',
                             candidate=EMPLOYEES.get(candidate_id, {}),
                             candidate_id=candidate_id,
                             voter_id=actual_voter_id,
                             is_director=is_director_vote,
                             flag=FLAG if is_director_vote else None,
                             current_employee=EMPLOYEES[CURRENT_USER])

@app.route('/leaderboard')
def leaderboard():
    sorted_employees = sorted(
        [(k, v) for k, v in EMPLOYEES.items() if v['role'] == 'Staff'],
        key=lambda x: x[1]['votes'],
        reverse=True
    )
    return render_template('leaderboard.html',
                         employees=sorted_employees,
                         current_employee=EMPLOYEES[CURRENT_USER])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5008)
