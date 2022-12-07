from flask import Flask,render_template,request,jsonify
import pandas as pd
from joblib import load

# =[Variabel Global]=============================

app   = Flask(__name__, static_url_path='/static', template_folder='template')
model = None

# =[Routing]=====================================

# [Routing untuk Halaman Result]
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about", methods=['GET'])
def about():
	return render_template('about.html')

@app.route("/job", methods=['GET'])
def job():
	return render_template('job.html')

@app.route("/test", methods=['GET'])
def test():
	return render_template('test.html')

@app.route("/result", methods=['GET'])
def result():
	return render_template('result.html')

# [Routing untuk API]	
@app.route("/hasil",methods=['POST'])
def hasil():
	# Nilai default untuk variabel input atau features (X) ke model
	# input_sepal_length = 5.1
	# input_sepal_width  = 3.5
	# input_petal_length = 1.4
	# input_petal_width  = 0.2

	if request.method=='POST':
		# Set nilai untuk variabel input atau features (X) berdasarkan input dari pengguna
		certificate = int(request.form['certificate'])
		workshop  = int(request.form['workshop'])
		memory = int(request.form['memory'])
		interested_subject  = int(request.form['interested_subject'])
		career_area = int(request.form['career_area'])
		company  = int(request.form['company'])
		work_in_team = int(request.form['work_in_team'])
		
		# Prediksi kelas Suggested Job Role berdasarkan data inputan yg diberikan pengguna
		df_test = pd.DataFrame(data={
														"certifications_code" : [certificate],
														"workshop_code"  : [workshop],
														"memory capability score_code" : [memory],
														"Interested subjects_code"  : [interested_subject],
														"interested career area _code"  : [career_area],
														"Type of company want to settle in?_code" : [company],
														"worked in teams ever?_code"  : [work_in_team]
													})

		hasil_prediksi = model.predict(df_test[0:1])[0]

		# Set Path untuk gambar hasil prediksi
		if hasil_prediksi == 'Network Security Engineer':
			gambar_prediksi = 'static/images/job/net-security-eng.png'
			desc = 'Bertanggung jawab untuk melindungi jaringan internal perusahaan atau kantor. Bertugas untuk mendeteksi, menyelidiki, dan mencegah gangguan yang mungkin dapat terjadi di sistem. Seorang network security engineer harus memastikan tidak adanya kebocoran data yang terjadi di jaringan.'
		elif hasil_prediksi == 'Software Engineer':
			gambar_prediksi = 'static/images/job/software-eng.png'
			desc = 'Bertanggung jawab untuk mengembangkan sistem, program, dan perangkat lunak dalam perusahaan. Software engineer dibutuhkan untuk menganalisis kebutuhan dan desain pengguna, konstruksi, serta uji aplikasi. Biasanya bekerja sama dengan software developer, programmer, dan spesialis quality control.'
		elif hasil_prediksi == 'UX Designer':
			gambar_prediksi = 'static/images/job/ux-designer.png'
			desc = 'Bertanggung jawab dalam menentukan apa pengalaman terbaik untuk pengguna dalam menggunakan suatu produk, misal website atau aplikasi. UX designer harus memastikan kegunaan, aksesibilitas, dan interaksi suatu aplikasi/situs menjadi user friendly.'
		elif hasil_prediksi == 'Software Developer':
			gambar_prediksi = 'static/images/job/software-dev.png'
			desc = 'Bertanggung jawab membangun serta menicptakan suatu produk. Sering bekerja sama dengan software engineer.'
		elif hasil_prediksi == 'Database Developer':
			gambar_prediksi = 'static/images/job/database-dev.png'
			desc = 'Bertanggung jawab terhadap problem yang terdapat di dalam aplikasi yang berhubungan dengan database. Database developer berfokus untuk mengelola sistem database.'
		elif hasil_prediksi == 'Software Quality Assurance (QA) / Testing':
			gambar_prediksi = 'static/images/job/testing-qa.png'
			desc = 'Bertanggung jawab terhadap perencanaan jaminan kualitas aplikasi agar terhindar dari kegagalan pada saat dijalankan. Juga agar software tersebut dipastikan sudah berjalan dengan baik sebelum sampai ke tangan customer.'
		elif hasil_prediksi == 'Web Developer':
			gambar_prediksi = 'static/images/job/web-dev.png'
			desc = 'Bertanggung jawab membuat dan mengembangkan situs. Selain itu web developer juga memastikan performa website optimal. Terdapat jenis-jenis web developer: back-end developer, front-end developer, dan full-stack developer.'
		elif hasil_prediksi == 'CRM Technical Developer':
			gambar_prediksi = 'static/images/job/crm-tech.png'
			desc = 'Bertanggung jawab terhadap pengembangan perangkat lunak yang mengimplementasikan perangkat tambahan untuk sistem CRM. Tidak jarang pula CRM Developer bertugas untuk merancang dan membuat modul tambahan, plugin khusus, atau rangkaian aplikasi perangkat lunak yang dapat diintegrasikan dengan sistem CRM.'
		elif hasil_prediksi == 'Technical Support':
			gambar_prediksi = 'static/images/job/tech-support.png'
			desc = 'Bertanggung jawab untuk membantu menyelesaikan masalah yang dihadapi user. Masalah user bisa berupa keluhan maupun pertanyaan.'
		elif hasil_prediksi == 'Systems Security Administrator':
			gambar_prediksi = 'static/images/job/system-sec-admin.png'
			desc = 'Bertanggung jawab terhadap keamanan jaringan komputer, termasuk keamanan dari sebuah administrasi sebuah perangkat seperti firewalls.'
		elif hasil_prediksi == 'Applications Developer':
			gambar_prediksi = 'static/images/job/app-dev.png'
			desc = 'Bertanggung jawab terhadap pembuatan dan pengujian aplikasi yang didesain khusus untuk suatu perangkat. Applications developer biasanya memiliki spesialisasinya sendiri. Misal ada developer yang fokus pada app dengan sistem operasi iOS.'
		elif hasil_prediksi == 'Mobile Applications Developer':
			gambar_prediksi = 'static/images/job/mobile-app-dev.png'
			desc = 'Bertanggung jawab terhadap pembuatan dan pengujian aplikasi yang didesain khusus untuk perangkat mobile. Mobile app developer umumnya terdapat spesialisasi sistem operasi iOS dan Android.'

		# Return hasil prediksi dengan format JSON
		return render_template('result.html', prediksi=hasil_prediksi, gambar_prediksi = gambar_prediksi, desc = desc)


# =[Main]========================================

if __name__ == '__main__':
	# Load model yang telah ditraining
	model = load('model_job_dt.model')

	# Run Flask di localhost 
	# app.run(debug=True)
	app.run(host="127.0.0.1", port=5020, debug=True)
