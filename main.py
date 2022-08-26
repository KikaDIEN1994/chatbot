from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	"""text = request.args.get('button_text')
	print()
	print('Button text:', text)
	print()"""
	return render_template("index.html")

@app.route('/question', methods=['POST'])
def question():
	if request.method=='POST':
		print(request.form.get('data_question'))
		return('',204)

if __name__ == "__main__":
	app.run(debug=True)