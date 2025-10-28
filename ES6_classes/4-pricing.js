export default class Pricing {
	_amount
	_currency
	constructor(amount, currency) {
		this._amount = amount
		this._currency = currency
	}
	get amount(){
		return this._amount
	}
	get currency(){
		return this._currency
	}
	set amount(v){
		this._amount = v
	}
	set currency(v){
		this._currency = v
	}

	displayFullPrice() {
		return `${this._amount} ${this._currency.displayFullCurrency()}`
	}
	static convertPrice(amount, conversionRate) {
		return amount * conversionRate
	}
}
