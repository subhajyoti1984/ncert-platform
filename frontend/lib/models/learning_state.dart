class LearningState {
  final String conceptId;
  final String status;

  LearningState({
    required this.conceptId,
    required this.status,
  });

  factory LearningState.fromJson(Map<String, dynamic> json) {
    return LearningState(
      conceptId: json["concept_id"],
      status: json["result"],
    );
  }
}
