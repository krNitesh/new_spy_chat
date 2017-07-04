from steganography.steganography import Steganography
Steganography.encode("input.jpeg","output.jpeg","message")
print Steganography.decode("output.jpeg")