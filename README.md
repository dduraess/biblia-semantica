# rascunho-projetos

Mais de 400 milhões de pessoas de língua portuguesa:

	- nenhuma concordância exaustiva do original grego/hebraico para português
	- nenhuma Bíblia com mecanismo de busca semantica em português


	features:

		exibição com pequenos nrs de versículo e quebra em parágrafo, onde: se in_fim_paragrafo for null não quebrar; se in_fim_paragrafo for 'S' quebra com espaçamento padrão; se in_fim_paragrafo for texto, exibir comentário do Autor (p.ex. preâmbulo do salmo 18) com espaçamento antes e depois

		Tanakh
		=> hebraico fonte média com dicionário português # (inicialmente só Strong *) no tool tip e concordância Tanakh no click / português fonte destacada / grego septuaginta fonte menor com dicionario português (*) no tool tip e concordância NT ao clicar

			# dicionário (tool tip) hebraico deve conter definição com sinônimos e transliteração (copiar de bibleforge.org e https://hebraico.pro.br/r/dicionariohebraico.asp?qs_idioma=HEBRAICO&qs_palavra=tyXarb) para português
			# concordância (click) deve conter nr ocorrencias da palavra e nr versículos em que a mesma ocorre sumarizado pelo original e pela LXX (copiar de Igor apps)

		NT
		=> grego fonte média com dicionário para português no tool tip e concordância LXX + NT no click / português fonte destacada

			# dicionário (tool tip) grego deve conter definição com sinônimos e transliteração (copiar de biblehub e bibleforge.org) para português
			# concordância (click) deve conter nr ocorrencias da palavra e nr versículos em que a mesma ocorre sumarizado pelo original e pela LXX (copiar de Igor apps)

		- Busca semântica em portugues com treinamento de alguma biblioteca de NLP (curso IBM no coursera)

		- Ver se dá pra usar a busca semantica pra extrair frases do seu contexto bíblico num dado arquivo de audio e/ou numa base de texto/audio

	MVP

		Tanakh + LXX tooltip apenas com strongs (*)
		Novo Testamento koine *
