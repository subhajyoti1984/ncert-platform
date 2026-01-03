ElevatedButton(
  onPressed: () async {
    final url = await ApiService.createCheckout();
    launchUrl(Uri.parse(url));
  },
  child: Text("Unlock Full Access"),
);
