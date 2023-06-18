const paymentBtn = document.getElementById('paystack-btn')
const reference_ = JSON.parse(document.getElementById('reference').textContent);
const email_ = JSON.parse(document.getElementById('email').textContent);
const amount_ = JSON.parse(document.getElementById('amount').textContent);
const key_ = JSON.parse(document.getElementById('key').textContent);
const verifyPaymentUrl = document.getElementById('verify-payment-url').dataset.url;


const payWithPayStack = () => {
    const currency = 'GHS';
    const plan = '';

    const obj = {
        key: key_,
        email: email_,
        amount: amount_ * 100,
        ref: reference_,

        callback: function (response) {
            window.location.href = verifyPaymentUrl
        }
    }

    if (Boolean(currency)) {
        obj.currency = currency.toUpperCase()
    }
    if (Boolean(plan)) {
        obj.plan = plan
    }

    let handler = PaystackPop.setup(obj);
    handler.openIframe();
}

paymentBtn.addEventListener('click', () => payWithPayStack())