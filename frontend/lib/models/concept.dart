class Concept {
  final String id;
  final String title;
  final String explanation;

  Concept({
    required this.id,
    required this.title,
    required this.explanation,
  });

  factory Concept.fromJson(Map<String, dynamic> json) {
    return Concept(
      id: json["concept_id"],
      title: json["title"] ?? "Concept",
      explanation: json["explanation"] ?? "",
    );
  }
}
