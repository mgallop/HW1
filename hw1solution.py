import unittest
import hw1

class TestInClassCode(unittest.TestCase):
  
  def setUp(self):
    return
  
  def test_kobe(self):
    self.assertEqual(hw1.shout("kobe"), "KOBE!")
  
  def test_rings(self):
    self.assertEqual(hw1.shout("ringz?"), "RINGZ!")
    
  def test_BRON(self):
    self.assertEqual(hw1.shout("LeBron."), "LEBRON!")
#shout fails
#AssertionError: 'LEBRON.' != 'LEBRON!' AssertionError: 'RINGZ!!' != 'RINGZ!'
  
  def test_norb(self):
    self.assertEqual(hw1.reverse("LeBron"), "norBeL")
  
  def test_multiplewords(self):
    self.assertEqual(hw1.reverse("penis attack"), "kcatta sinep")
    
  def test_of_characters(self):
    self.assertEqual(hw1.reverse("why.does?MYpunc\\tuationsuck???"), "???kcusnoitaut\\cnupYM?seod.yhw")

#reverse passes    
  def test_single(self):
    self.assertEqual(hw1.reversewords("This is just one sentence"), "sentence one just is This. ")
  
  def test_multiple(self):
    self.assertEqual(hw1.reversewords("I hope this program can distinguish between multiple sentences. Otherwise it is dumb."), "sentences multiple between distinguish can program this hope I. dumb is it Otherwise. ")
    
  def test_of_punctuation(self):
    self.assertEqual(hw1.reversewords("Exclamation point! Question mark? Do these work here? No."), "point Exclamation! mark Question? here work these Do? No. ")

#Reverse Words Fails
#AssertionError: 'point Exclamation. mark Question. here work these Do. No. ' != point Exclamation! mark Question? here work these Do? No. '
  def test_palindrome(self):
    self.assertEqual(hw1.reversewordletters("Never odd or even."), "reveN ddo ro neve.")

  def leet(self):
    self.assertEqual(hw1.reversewordletters("Th1s h@ndles t3h 1337sp3ak."), "s1hT seldn@h h3t ka3ps7331.")
    
  def test_reverseletterpunctuation(self):
    self.assertEqual(hw1.reversewordletters("Did this one get punctuation marks right? No!"), "diD siht eno teg noitautcnup skram thgir? oN!")
#Reverse Word Letters works

  def test_test(self):
    self.assertEqual(hw1.piglatin("test"), "estte")
  
  def test_piglatin(self):
    self.assertEqual(hw1.piglatin("pig latin"), "igpe atinle")
    
  def test_ireadthecode(self):
    self.assertEqual(hw1.piglatin("I read how you defined this function"), "Ie eadre owhe ouye efinedde isthe unctionfe")
#piglatin fails, obviously    
if __name__ == '__main__':
  unittest.main()
  
