import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  static String? token;

  static Future<String?> login(String email, String password) async {
    final res = await http.post(
      Uri.parse("http://127.0.0.1:8000/api/v1/auth/login"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "email": email,
        "password": password
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
