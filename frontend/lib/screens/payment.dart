import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import '../services/api.dart';

class PaymentScreen extends StatelessWidget {
  final String token;

  const PaymentScreen({
    Key? key,
    required this.token,
  }) : super(key: key);

  Future<void> _startPayment(BuildContext context) async {
    try {
      final url = await ApiService.createCheckout(token);
      final uri = Uri.parse(url);

      if (!await launchUrl(
        uri,
        mode: LaunchMode.externalApplication,
      )) {
        throw Exception("Could not launch payment URL");
      }
    } catch (e) {
      debugPrint("Payment error: $e");
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Payment failed")),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Unlock Full Access")),
      body: Center(
        child: ElevatedButton(
          onPressed: () => _startPayment(context),
          child: const Text("Proceed to Payment"),
        ),
      ),
    );
  }
}
