import 'package:flutter/material.dart';
import 'screens/login.dart';
import 'screens/chapter_list.dart';
import 'screens/learning_loop.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (_) => const LoginScreen(),
        '/chapters': (_) => const ChapterListScreen(),
        '/learn': (_) => const LearningLoopScreen(),
      },
    );
  }
}
