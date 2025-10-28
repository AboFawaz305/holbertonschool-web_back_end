export default class Car {
	_brand
	_motor
	_color
	constructor(brand, motor, color){
		this._brand = brand
		this._motor = motor
		this._color = color
	}
	get brand(){
		return this._brand
	}
	get motor(){
		return this._motor
	}
	get color(){
		return this._color
	}
	set brand(v){
		this._brand = v
	}
	set motor(v){
		this._motor = v
	}
	set color(v){
		this._color = v
	}

	cloneCar(){
		return new this.constructor(this._brand, this._motor, this._color)
	}
}

