import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
	_floors
	constructor(sqft, floors){
		super(sqft)
		this._floors = floors
	}

	get floors(){
		return this._floors
	}
	set floors(v){
		this._floors = v
	}

	evacuationWarningMessage(){
		return `Evacuate slowly the ${this._floors} floors`
	}
}
