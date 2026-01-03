import 'package:flutter/material.dart';

class ChapterListScreen extends StatelessWidget {
  const ChapterListScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Chapters")),
      body: ListView(
        children: [
          ListTile(
            title: const Text("Chapter 2: Polynomials"),
            onTap: () {
              Navigator.pushNamed(context, '/learn');
            },
          )
        ],
      ),
    );
  }
}
