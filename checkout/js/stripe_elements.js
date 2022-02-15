/*
Core logic/payment for this comes from:
https://stripe.com/docs/stripe-js/appearance-api

Css from here:
https//stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
const appearance = {
    theme: 'stripe',
    variables: {
      colorPrimary: '#0c343d',
    },
  };
var card = elements.create('card', {appearance: appearance});
card.mount('#card-element');