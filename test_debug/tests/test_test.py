class TestSuite():

    def test_case_1(self, case_data):
        time = int(case_data)
        print("   > Received from fixture timestamp is: {}".format(time))
        assert(time % 2 == 0)