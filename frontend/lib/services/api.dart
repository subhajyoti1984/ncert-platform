import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "http://127.0.0.1:8000";

  static Future<Map<String, dynamic>> startSection() async {
    final res = await http.get(
      Uri.parse("$baseUrl/api/v1/learning/section/start"),
    );
    return jsonDecode(res.body);
  }

  static Future<Map<String, dynamic>> submitAnswer(
      String answer) async {
    final res = await http.post(
      Uri.parse("$baseUrl/api/v1/learning/section/answer"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "student_answer": answer
      }),
    );
    return jsonDecode(res.body);
  }
}
