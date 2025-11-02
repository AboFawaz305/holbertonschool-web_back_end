export default function updateStudentGradeByCity(stds, location, stdGrades) {
  return stds
    .filter((e) => e.location === location)
    .map((std) => {
      const stdGrade = stdGrades.find((sg) => sg.studentId === std.id);
      let grade = "N/A";
      if (stdGrade) grade = stdGrade.grade;
      return { ...std, grade: grade };
    });
}
