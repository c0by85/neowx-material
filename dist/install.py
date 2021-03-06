# installer for the neowx-material skin

from setup import ExtensionInstaller

def loader():
    return BasicInstaller()

class BasicInstaller(ExtensionInstaller):
    def __init__(self):
        super(BasicInstaller, self).__init__(
            version="1.0",
            name='neowx-material',
            description='The most versatile and modern weewx skin',
            author="Neoground GmbH",
            author_email="weather@neoground.com",
            config={
                'StdReport': {
                    'StandardReport': {
                        'skin':'neowx-material'
                    }
                }
            },
            files=[('skins/neowx-material',
                    ['skins/neowx-material/almanac.html.tmpl',
                    'skins/neowx-material/archive.html.tmpl',
                    'skins/neowx-material/footer.inc',
                    'skins/neowx-material/graph_area_archive_config.inc',
                    'skins/neowx-material/graph_area_config.inc',
                    'skins/neowx-material/graph_bar_archive_config.inc',
                    'skins/neowx-material/graph_bar_config.inc',
                    'skins/neowx-material/graph_radar_config.inc',
                    'skins/neowx-material/graphs.inc',
                    'skins/neowx-material/head.inc',
                    'skins/neowx-material/header.inc',
                    'skins/neowx-material/index.html.tmpl',
                    'skins/neowx-material/js.inc',
                    'skins/neowx-material/manifest.json',
                    'skins/neowx-material/month-%Y-%m.html.tmpl',
                    'skins/neowx-material/month.html.tmpl',
                    'skins/neowx-material/skin.conf',
                    'skins/neowx-material/telemetry.html.tmpl',
                    'skins/neowx-material/week.html.tmpl',
                    'skins/neowx-material/year-%Y.html.tmpl',
                    'skins/neowx-material/year.html.tmpl',
                    'skins/neowx-material/yesterday.html.tmpl',
                    'skins/neowx-material/archive/NOAA-%Y.txt.tmpl',
                    'skins/neowx-material/archive/NOAA-%Y-%m.txt.tmpl',
                    'skins/neowx-material/css/bootstrap.min.css',
                    'skins/neowx-material/css/style.min.css',
                    'skins/neowx-material/fonts/OFL.txt',
                    'skins/neowx-material/fonts/Rubik-Light.eot',
                    'skins/neowx-material/fonts/Rubik-Light.woff',
                    'skins/neowx-material/fonts/Rubik-Light.woff2',
                    'skins/neowx-material/fonts/Rubik-Regular.eot',
                    'skins/neowx-material/fonts/Rubik-Regular.woff',
                    'skins/neowx-material/fonts/Rubik-Regular.woff2',
                    'skins/neowx-material/img/icon-32.png',
                    'skins/neowx-material/img/icon-48.png',
                    'skins/neowx-material/img/icon-72.png',
                    'skins/neowx-material/img/icon-96.png',
                    'skins/neowx-material/img/icon-120.png',
                    'skins/neowx-material/img/icon-128.png',
                    'skins/neowx-material/img/icon-144.png',
                    'skins/neowx-material/img/icon-152.png',
                    'skins/neowx-material/img/icon-168.png',
                    'skins/neowx-material/img/icon-192.png',
                    'skins/neowx-material/img/icon-256.png',
                    'skins/neowx-material/img/icon-512.png',
                    'skins/neowx-material/img/icon-alpha-1x.png',
                    'skins/neowx-material/img/icon-alpha-2x.png',
                    'skins/neowx-material/js/app.js',
                    'skins/neowx-material/js/bootstrap.min.js',
                    'skins/neowx-material/js/jquery.min.js',
                    'skins/neowx-material/js/mdb.min.js',
                    'skins/neowx-material/js/popper.min.js',
                    'skins/neowx-material/js/modules/wow.min.js',
                    'skins/neowx-material/js/vendor/moment.min.js',
                    'skins/neowx-material/js/vendor/moment-with-locales.min.js',
                    'skins/neowx-material/js/vendor/apexcharts/apexcharts.min.js',
                    'skins/neowx-material/js/vendor/apexcharts/locales/ca.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/cs.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/de.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/el.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/en.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/es.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/fi.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/fr.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/he.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/hi.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/hr.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/hy.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/id.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/it.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/ka.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/ko.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/lt.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/nb.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/nl.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/pl.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/pt.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/pt-br.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/rs.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/ru.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/se.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/sk.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/sl.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/sq.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/th.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/tr.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/ua.json',
                    'skins/neowx-material/js/vendor/apexcharts/locales/zh-cn.json',
                    'skins/neowx-material/weather-icons/css/weather-icons.css',
                    'skins/neowx-material/weather-icons/css/weather-icons.min.css',
                    'skins/neowx-material/weather-icons/css/weather-icons-wind.css',
                    'skins/neowx-material/weather-icons/css/weather-icons-wind.min.css',
                    'skins/neowx-material/weather-icons/font/weathericons-regular-webfont.eot',
                    'skins/neowx-material/weather-icons/font/weathericons-regular-webfont.svg',
                    'skins/neowx-material/weather-icons/font/weathericons-regular-webfont.ttf',
                    'skins/neowx-material/weather-icons/font/weathericons-regular-webfont.woff',
                    'skins/neowx-material/weather-icons/font/weathericons-regular-webfont.woff2']),
            ]
            )