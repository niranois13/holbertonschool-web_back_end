export default function getStudentIdsSum(students) {
  return students
    .map((student) => student.id)
    .reduce((initialValue, currentValue) => initialValue + currentValue);
}
