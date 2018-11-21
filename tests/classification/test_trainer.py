import os
import shutil
import unittest
from gcn.classification.trainer import Trainer
from gcn.language_model.baseline import LSTMLM


class TestTrainer(unittest.TestCase):

    def test_download(self):
        root = os.path.join(os.path.dirname(__file__), "../../")
        trainer = Trainer(root)
        r = trainer.download()
        self.assertTrue(r)

    def test_build(self):
        root = os.path.join(os.path.dirname(__file__), "../../")
        trainer = Trainer(root, preprocessor_name="test_tc_preprocessor")

        trainer.build()
        self.assertTrue(len(trainer.preprocessor.vocabulary.get()) > 1000)
        print(trainer.preprocessor.vocabulary.get()[:100])
        print(trainer.preprocessor_path)
        os.remove(trainer.preprocessor_path)

    def test_train(self):
        pass
