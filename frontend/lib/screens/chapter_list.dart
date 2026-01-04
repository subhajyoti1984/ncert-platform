import 'package:flutter/material.dart';
import 'learning_loop.dart';

class ChapterListScreen extends StatelessWidget {
  final String token;

  const ChapterListScreen({
    Key? key,
    required this.token,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Chapters")),
      body: ListView(
        children: [
          ListTile(
            title: const Text("Chapter 2: Polynomials"),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => LearningLoopScreen(token: token),
                ),
              );
            },
          ),
        ],
      ),
    );
  }
}
