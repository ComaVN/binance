from util import binance
import unittest

class UtilBinanceTestCase(unittest.TestCase):

    unittest.TestCase.maxDiff = None

    def test_get_asset_from_trading_pair_ETH(self):
        self.assertEqual(binance.get_asset_from_trading_pair("FOOETH"), "FOO")
        self.assertEqual(binance.get_asset_from_trading_pair("FOO_ETH"), "FOO")
        self.assertEqual(binance.get_asset_from_trading_pair("FOO-ETH"), "FOO")
        self.assertEqual(binance.get_asset_from_trading_pair("FOO.ETH"), "FOO")
        self.assertEqual(binance.get_asset_from_trading_pair("FOO ETH"), "FOO")
        self.assertEqual(binance.get_asset_from_trading_pair("NANOETH"), "NANO")
        self.assertEqual(binance.get_asset_from_trading_pair("NANO_ETH"), "NANO")
        self.assertEqual(binance.get_asset_from_trading_pair("NANO-ETH"), "NANO")
        self.assertEqual(binance.get_asset_from_trading_pair("NANO.ETH"), "NANO")
        self.assertEqual(binance.get_asset_from_trading_pair("NANO ETH"), "NANO")

    def test_get_asset_from_trading_pair_BTC(self):
        self.assertEqual(binance.get_asset_from_trading_pair("ETHBTC"), "ETH")
        self.assertEqual(binance.get_asset_from_trading_pair("FOOBTC"), "FOO")

    def test_get_asset_from_trading_pair_USDT(self):
        self.assertEqual(binance.get_asset_from_trading_pair("ETHUSDT"), "ETH")
        self.assertEqual(binance.get_asset_from_trading_pair("FOOUSDT"), "FOO")

    def test_get_asset_from_trading_pair_BNB(self):
        self.assertEqual(binance.get_asset_from_trading_pair("ETHBNB"), "ETH")
        self.assertEqual(binance.get_asset_from_trading_pair("FOOBNB"), "FOO")

    def test_get_asset_from_trading_pair_unknown_market(self):
        self.assertRaises(ValueError, lambda: binance.get_asset_from_trading_pair("ETHFOO"))

    def test_get_market_from_trading_pair_ETH(self):
        self.assertEqual(binance.get_market_from_trading_pair("FOOETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("FOO_ETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("FOO-ETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("FOO.ETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("FOO ETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("NANOETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("NANO_ETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("NANO-ETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("NANO.ETH"), "ETH")
        self.assertEqual(binance.get_market_from_trading_pair("NANO ETH"), "ETH")

    def test_get_market_from_trading_pair_BTC(self):
        self.assertEqual(binance.get_market_from_trading_pair("ETHBTC"), "BTC")
        self.assertEqual(binance.get_market_from_trading_pair("FOOBTC"), "BTC")

    def test_get_market_from_trading_pair_USDT(self):
        self.assertEqual(binance.get_market_from_trading_pair("ETHUSDT"), "USDT")
        self.assertEqual(binance.get_market_from_trading_pair("FOOUSDT"), "USDT")

    def test_get_market_from_trading_pair_BNB(self):
        self.assertEqual(binance.get_market_from_trading_pair("ETHBNB"), "BNB")
        self.assertEqual(binance.get_market_from_trading_pair("FOOBNB"), "BNB")

    def test_get_market_from_trading_pair_unknown_market(self):
        self.assertRaises(ValueError, lambda: binance.get_market_from_trading_pair("ETHFOO"))
