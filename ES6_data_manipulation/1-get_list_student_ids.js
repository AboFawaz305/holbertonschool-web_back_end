export default function getListStudentIds(stds){
	if (!Array.isArray(stds))
		return [];
	return stds.map((e) => e.id)
}
