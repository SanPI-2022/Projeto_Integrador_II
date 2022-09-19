function mudaTela1(){
	    window.location.href = "telab"
	}

function mudaAdministrativa(){
	    window.location.href = "administrativa"
	}

function mudaLogin(){
        window.location.href = "login"
	}

function mudaTelaGerarQrcode(){
	    window.location.href = "inicio"
	}

function mudaReclamacoes(){
	    window.location.href = "reclamacoes"
	}

function mudaTelaCadPostes(){
	    window.location.href = "../cadastraposte"
	}

function mudaPostesCadastrados(){
	    window.location.href = "postescadastrados"
	}

function cadastrei(){
//        alert("Cadastrado com sucesso!");
	    window.location.href = "cadastraposte"
	}

function mudaTelaCadUsuario(){
	    window.location.href = "register"
	}

function mudaQrcode(){
	    window.location.href = "telaqrs"
	}

function mudaTelaN(){
	    window.location.href = "telab"
	}

function mudaTela2(){
	    window.location.href = "telac"
	}

function mudaTela3(){
	    window.location.href = "telad"
	}

function mudaTela4(){
	    window.location.href = "telae"
	}
	
function copiarProtocolo() {
		let copiadoProtocolo = document.getElementById("protocolo");
		copiadoProtocolo.select();
		copiadoProtocolo.setSelectionRange(0, 99999);
		
		document.execCommand("copy");
		alert("Copiado protocolo para área de transferência: " + copiadoProtocolo.value);
        }

function mudaTela5(){
	    window.location.href = "/"
	}

function voltaAdministrativa(){
	    window.location.href = "../administrativa"
	}

function mudaTelaC(){
	    window.location.href = "/"
	}

function mudaTelaCCP(){
	    window.location.href = "../administrativa"
	}

function mudaTelaVoltaAoBancoPos(){
	    window.location.href = "../postescadastrados"
	}

function mudaTelaVoltaAoBancoPro(){
	    window.location.href = "../reclamacoes"
	}
