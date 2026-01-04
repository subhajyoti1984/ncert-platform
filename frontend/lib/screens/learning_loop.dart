import 'package:flutter/material.dart';
import '../services/api.dart';

class LearningLoopScreen extends StatefulWidget {
  final String token; // passed after login

  const LearningLoopScreen({Key? key, required this.token}) : super(key: key);

  @override
  State<LearningLoopScreen> createState() => _LearningLoopScreenState();
}

class _LearningLoopScreenState extends State<LearningLoopScreen> {
  String? conceptId;
  String explanation = "";
  final TextEditingController _answerCtrl = TextEditingController();
  bool loading = true;

  @override
  void initState() {
    super.initState();
    _loadNextConcept();
  }

  Future<void> _loadNextConcept() async {
    setState(() => loading = true);

    final data = await ApiService.startSection(widget.token);

    setState(() {
      conceptId = data["concept_id"];
      explanation = data["explanation"] ?? "Explain the concept here.";
      loading = false;
      _answerCtrl.clear();
    });
  }

  Future<void> _submitAnswer() async {
    if (conceptId == null) return;

    await ApiService.submitAnswer(
      token: widget.token,
      conceptId: conceptId!,
      answer: _answerCtrl.text,
    );

    await _loadNextConcept();
  }

  @override
  Widget build(BuildContext context) {
    if (loading) {
      return const Scaffold(
        body: Center(child: CircularProgressIndicator()),
      );
    }

    return Scaffold(
      appBar: AppBar(title: const Text("Learning")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              "Concept",
              style: Theme.of(context).textTheme.titleLarge,
            ),
            const SizedBox(height: 12),
            Text(explanation),
            const SizedBox(height: 20),
            TextField(
              controller: _answerCtrl,
              decoration: const InputDecoration(
                labelText: "Your Answer",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _submitAnswer,
              child: const Text("Submit & Continue"),
            ),
          ],
        ),
      ),
    );
  }
}
