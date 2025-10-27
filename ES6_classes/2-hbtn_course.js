export default class HolbertonCourse {
	_name;
	_length;
	_students;
	constructor (name, length, students) {
		this.name = name;
		this.length = length;
		this.students = students;
	}
	get name(){
		return this._name
	}
	get length(){
		return this._length
	}
	get students(){
		return this._students
	}
	set name(value){
		if (typeof (value) !== 'string')
			throw new TypeError("Name must be a string")
		this._name = value
	}
	set length(value){
		if (typeof (value) !== 'number')
			throw new TypeError("Length must be a number")
		this._length = value
	}
	set students(value){
		if (
			(!Array.isArray(value)) ||
			(value.reduce((a, c) => a && typeof (c) !== 'string', false))
		)
			throw new TypeError("Students must be an array of strings")
		this._students = value
	}

}
