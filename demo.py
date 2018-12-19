# python demo.py --checkpoint tacotron/tmp/tacotron-20180906/model.ckpt --text "Hello Richmond" --output Richmond.wav

from tacotron.synthesizer import Synthesizer
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--checkpoint', required=False, help='Full path to model checkpoint', default="tacotron/tmp/tacotron-20180906/model.ckpt")
parser.add_argument('--text', required=False, help='Text to synthesize', default="Hello World")
parser.add_argument('--output', required=False, help='File path of output', default="HelloWorld.wav")
args = parser.parse_args()


checkpoint = str(args.checkpoint)
text = str(args.text)
output = str(args.output)
print("Checkpoint: " + checkpoint)
print("Text: " + text)
print("Output: " + output)
print("")

print("Loading model...")
synthesizer = Synthesizer()
synthesizer.load(checkpoint)
print("Loading model completed!")
print("")

print("Sythesizing text...")
with open(output, 'wb') as file:
    file.write(synthesizer.synthesize(text))
print("Sythesizing text completed!")
print("")

