export default class Airport{
	_name
	_code
	constructor(name, code){
		this._name = name
		this._code = code
	}

	get name(){
		return this._name
	}
	get code(){
		return this._code
	}
	set name(v){
		this._name = v
	}
	set code(v){
		this._code = v
	}

	get [Symbol.toStringTag](){
		return this._code
	}
}
