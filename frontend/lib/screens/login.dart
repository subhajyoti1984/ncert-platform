import 'package:flutter/material.dart';
import '../services/auth.dart';
import 'chapter_list.dart'; // adjust path if needed

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  String email = "";
  String password = "";
  bool loading = false;
  String? error;

  Future<void> login() async {
    setState(() {
      loading = true;
      error = null;
    });

    try {
      final token = await AuthService.login(email, password);

      if (token == null) {
        setState(() {
          error = "Invalid credentials";
          loading = false;
        });
        return;
      }

      // ✅ Pass token forward explicitly
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (_) => ChapterListScreen(token: token),
        ),
      );
    } catch (e) {
      setState(() {
        error = "Login failed";
        loading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Login")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              onChanged: (v) => email = v,
              decoration: const InputDecoration(labelText: "Email"),
            ),
            TextField(
              onChanged: (v) => password = v,
              obscureText: true,
              decoration: const InputDecoration(labelText: "Password"),
            ),
            const SizedBox(height: 16),

            if (error != null)
              Text(
                error!,
                style: const TextStyle(color: Colors.red),
              ),

            const SizedBox(height: 8),

            ElevatedButton(
              onPressed: loading ? null : login,
              child: loading
                  ? const CircularProgressIndicator()
                  : const Text("Login"),
            ),
          ],
        ),
      ),
    );
  }
}
