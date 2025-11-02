export default function getStudentIdsSum(stds){
	return stds.reduce((acc, std) => acc + std.id, 0)
}
