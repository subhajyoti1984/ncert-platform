import 'package:flutter/material.dart';

class LearningLoopScreen extends StatefulWidget {
  const LearningLoopScreen({Key? key}) : super(key: key);

  @override
  State<LearningLoopScreen> createState() => _LearningLoopScreenState();
}

class _LearningLoopScreenState extends State<LearningLoopScreen> {
  String conceptTitle = "Polynomials in One Variable";
  String explanation =
      "A polynomial in one variable has only non-negative integer powers.";
  String answer = "";

  void submitAnswer() {
    print("Student answer: $answer");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Learning"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              conceptTitle,
              style: const TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 12),
            Text(explanation),
            const SizedBox(height: 16),
            TextField(
              onChanged: (v) => answer = v,
              decoration: const InputDecoration(
                labelText: "Your Answer",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: submitAnswer,
              child: const Text("Submit"),
            ),
          ],
        ),
      ),
    );
  }
}
