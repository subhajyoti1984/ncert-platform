import 'package:flutter/material.dart';
import 'screens/login.dart';
import 'screens/chapter_list.dart';
import 'screens/learning_loop.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      onGenerateRoute: (settings) {
        switch (settings.name) {
          case '/':
            return MaterialPageRoute(
              builder: (_) => const LoginScreen(),
            );

          case '/chapters':
            final token = settings.arguments as String;
            return MaterialPageRoute(
              builder: (_) => ChapterListScreen(token: token),
            );

          case '/learn':
            final token = settings.arguments as String;
            return MaterialPageRoute(
              builder: (_) => LearningLoopScreen(token: token),
            );

          default:
            return MaterialPageRoute(
              builder: (_) => const Scaffold(
                body: Center(child: Text('Route not found')),
              ),
            );
        }
      },
    );
  }
}
