export default class Building {
	_sqft
	constructor(sqft) {
		this._sqft = sqft
	}
	get sqft(){
		return this._sqft
	}
	set sqft(v){
		this._sqft = v
	}
	evacuationWarningMessage(){
		throw new Error("Class extending Building must override evacuationWarningMessage")
	}
}
