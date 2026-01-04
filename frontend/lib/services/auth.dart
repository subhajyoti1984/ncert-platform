import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  static String? token;

  static const String baseUrl =
      "https://ncert-backend-lu7s.onrender.com";

  static Future<String?> login(String email, String password) async {
    final res = await http.post(
      Uri.parse("$baseUrl/auth/login"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "email": email,
        "password": password,
      }),
    );

    if (res.statusCode == 200) {
      final data = jsonDecode(res.body);
      token = data["token"];
      return token;
    }

    return null;
  }
}
