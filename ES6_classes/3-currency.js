export default class Currency {
	_code
	_name
	constructor(code, name) {
		this._code = code
		this._name = name
	}

	get code(){
		return this._code
	}
	get name(){
		return this._name
	}
	set code(v){
		this._code = v
	}
	set name(v){
		this._name = v
	}

	displayFullCurrency(){
		return `${this._name} (${this._code})`
	}
}
