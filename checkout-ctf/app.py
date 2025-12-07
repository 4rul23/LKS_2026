from flask import Flask, request, render_template, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

FLAG = "STELKCSC{cl13nt_s1d3_pr1c3_m4n1pul4t10n}"

# Products database
PRODUCTS = {
    'legendary-key': {
        'id': 'legendary-key',
        'name': 'Legendary Loot Key',
        'description': 'Unlock exclusive legendary items in any supported game. One-time use.',
        'price': 999999,
        'image': 'legendary'
    },
    'season-pass': {
        'id': 'season-pass', 
        'name': 'Ultimate Season Pass',
        'description': 'Access all seasonal content, battle passes, and exclusive rewards.',
        'price': 499999,
        'image': 'season'
    },
    'vip-membership': {
        'id': 'vip-membership',
        'name': 'VIP Gamer Membership',
        'description': '1 year of premium benefits, early access, and bonus credits.',
        'price': 1499999,
        'image': 'vip'
    }
}

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/product/<product_id>')
def product(product_id):
    if product_id not in PRODUCTS:
        return redirect(url_for('index'))
    return render_template('product.html', product=PRODUCTS[product_id])

@app.route('/checkout/<product_id>')
def checkout(product_id):
    if product_id not in PRODUCTS:
        return redirect(url_for('index'))
    return render_template('checkout.html', product=PRODUCTS[product_id])

@app.route('/purchase', methods=['POST'])
def purchase():
    product_id = request.form.get('product_id', '')
    price = request.form.get('price', '0')
    
    try:
        price = int(price)
    except:
        price = 999999
    
    if product_id not in PRODUCTS:
        return redirect(url_for('index'))
    
    product = PRODUCTS[product_id]
    
    # Vulnerable: trusting client-provided price
    if price <= 0:
        # Free purchase - give them the flag!
        return render_template('success.html', 
                             product=product, 
                             paid=price,
                             flag=FLAG)
    else:
        return render_template('success.html',
                             product=product,
                             paid=price,
                             flag=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5006)
