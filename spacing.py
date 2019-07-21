from soyspacing.countbase import RuleDict, CountSpace

corpus_fname = 'sentences.txt'
model = CountSpace()
model.train(corpus_fname)
model.save_model("soispace.model")
