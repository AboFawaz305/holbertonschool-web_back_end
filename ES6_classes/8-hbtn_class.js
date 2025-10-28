export default class HolbertonClass{
	_size
	 _location
	constructor(size, location){
		this._size = size
		this._location = location
	}

	get size(){
		return this._size
	}
	set location(v){
		this._location = v
	}
	get size(){
		return this._size
	}
	set location(v){
		this._location = v
	}

	[Symbol.toPrimitive](type){
		if (type === "string")
			return this._location
		if (type === "number")
			return this._size
		return this._size
	}
}
