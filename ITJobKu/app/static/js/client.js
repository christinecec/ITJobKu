$(document).ready(function(){
    // Fungsi untuk memanggil API ketika tombol prediksi ditekan
    $("#prediksi_submit").click(function(e) {
        //e.preventDefault();
        
        // Set data dari input pengguna
        var certificate = document.getElementById("certificate").value;
        var workshop = document.getElementById("workshop").value;
        var memory = document.getElementById("memory").value;
        var interested_subject = document.getElementById("interested_subject").value;
        var career_area = document.getElementById("career-area").value;
        var company = document.getElementById("company").value;
        var work_in_team = document.getElementById("work-in-team").value;
        
        //console.log(certificate)
        // Panggil API dengan timeout 1 detik (1000 ms)
        setTimeout(function() {
            try {
                $.ajax({
                    url  : "/hasil",
                    type : "POST",
                    data : {"certificate" : certificate,
                            "workshop"  : workshop,
                            "memory" : memory,
                            "interested_subject"  : interested_subject,
                            "career_area"  : career_area,
                            "company" : company,
                            "work_in_team"  : work_in_team,
                        },
                    success:function(res){
                    // Ambil hasil prediksi spesies dan path gambar spesies dari API
                    res_data_prediksi   = res['prediksi']
                    res_gambar_prediksi = res['gambar_prediksi']
                    res_desc_prediksi   = res['desc']
                    
                    // Tampilkan hasil prediksi ke halaman web
                    generate_prediksi(res_data_prediksi, res_gambar_prediksi, res_desc_prediksi); 
                    }
                });
            }
            catch(e) {
                // Jika gagal memanggil API, tampilkan error di console
                console.log("Gagal !");
                console.log(e);
            } 
            }, 1000)

        // Fungsi untuk menampilkan hasil prediksi model
        function generate_prediksi(data_prediksi, image_prediksi, desc_prediksi) {
            var str="";
            str += '<img src="{{url_for("static", filename = "/images/job/"'+image_prediksi+')}}>';
            str += '<div class="test-title result-title">' + data_prediksi + '</div>';
            str += '<div class="about result-desc">' + desc_prediksi + '</div>';
            $("#result_prediksi").html(str);
        }
        
    })
//})
