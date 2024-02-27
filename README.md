# almeida-semantica

Mais de 400 milhões de pessoas de língua portuguesa:

	- nenhuma concordância exaustiva do original em português;
	- nenhuma Bíblia (que eu conheça) com referência cruzada AT/NT;
	- nenhuma Bíblia com mecanismo de busca semantica em português


	features:

		Antigo Testamento

		Hebraico => Português: HeBERT

		- Português ARA destacado: exibição com pequenos nrs de versículo e quebra em parágrafo, onde: se in_fim_paragrafo for null não quebrar; se in_fim_paragrafo for 'S' quebra com espaçamento padrão; se in_fim_paragrafo for texto, exibir comentário do Autor (p.ex. preâmbulo do salmo 18) com espaçamento antes e depois
		- Original Hebraico fonte pequena Hint Strong's traduzido português (NLP); link para modal concordância (frame 1: ocorrências no AT original hebraico; frame 2: ocorrências NT conf. LXX)

		Novo testamento

		Grego => Português: Spacy instalado ok

		- Português ARA destacado: exibição com pequenos nrs de versículo e quebra em parágrafo, onde: se in_fim_paragrafo for null não quebrar; se in_fim_paragrafo for 'S' quebra com espaçamento padrão; se in_fim_paragrafo for texto, exibir comentário do Autor (p.ex. preâmbulo do salmo 18) com espaçamento antes e depois
		- Original koine fonte pequena Hint Strong's traduzido português (NLP); link para modal concordância (frame 1: ocorrências original koine; frame 2: ocorrências AT conf. LXX)

		Misc NLP

		- Busca semântica em portugues p/extrair frases do seu contexto bíblico;

		- Tradução dos originais com referências em toda a bíblia pela Septuaginta;

		- Prever qual o autor da passagem https://www.youtube.com/watch?v=bMbjDi-JVkY;

		- Classificar o texto por tema (Teologia Sistemática);

	MVP

		Tradução automática MYMEMORY.TRANSLATED.NET do hebraico moderno da Tanack, baseado no projeto https://github.com/openscriptures/morphhb, derivado do Westiminster Leningrad Codex (domínio público)
		***TODO*** Tradução automática do Grego
		***TODO*** Verificar biblioteca (spacy, bert) que pode ser usado para treinar modelos de tradução para novas línguas  
		Tanakh + LXX tooltip apenas com strongs (*)
		Novo Testamento koine
