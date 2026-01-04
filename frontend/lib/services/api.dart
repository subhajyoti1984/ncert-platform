import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const baseUrl = "https://ncert-backend-lu7s.onrender.com";

  // -------------------------------
  // LEARNING: START SECTION
  // -------------------------------
  static Future<Map<String, dynamic>> startSection(String token) async {
    final res = await http.get(
      Uri.parse("$baseUrl/api/v1/learning/section/start"),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/json",
      },
    );

    if (res.statusCode != 200) {
      throw Exception("Failed to start section");
    }

    return jsonDecode(res.body);
  }

  // -------------------------------
  // LEARNING: SUBMIT ANSWER
  // -------------------------------
  static Future<void> submitAnswer({
    required String token,
    required String conceptId,
    required String answer,
  }) async {
    final res = await http.post(
      Uri.parse("$baseUrl/api/v1/learning/section/answer"),
      headers: {
        "Authorization": "Bearer $token",
        "Content-Type": "application/json",
      },
      body: jsonEncode({
        "concept_id": conceptId,
        "answer": answer,
      }),
    );

    if (res.statusCode != 200) {
      throw Exception("Answer submission failed");
    }
  }

  // -------------------------------
  // PAYMENTS: CREATE CHECKOUT
  // -------------------------------
  static Future<String> createCheckout(String token) async {
    final res = await http.post(
      Uri.parse("$baseUrl/api/v1/payments/checkout"),
      headers: {
        "Authorization": "Bearer $token",
        "Content-Type": "application/json",
      },
    );

    if (res.statusCode != 200) {
      throw Exception("Failed to create checkout session");
    }

    final data = jsonDecode(res.body);
    return data["checkout_url"];
  }
}
