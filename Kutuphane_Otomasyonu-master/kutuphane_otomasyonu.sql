-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 30 May 2021, 22:43:28
-- Sunucu sürümü: 10.4.17-MariaDB
-- PHP Sürümü: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `kutuphane_otomasyonu`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `adresler`
--

CREATE TABLE `adresler` (
  `ID` int(11) NOT NULL,
  `adres` varchar(100) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `adresler`
--

INSERT INTO `adresler` (`ID`, `adres`) VALUES
(1, 'Kütüphane Şube Müdürlüğü Setbaşı Köprüsü Yanı 16360   Yıldırım / BURSA'),
(2, 'Kayhan, 3. Koç Sk. No:10, 16020 Osmangazi/Bursa'),
(3, 'Ataevler, 16140 Nilüfer/Bursa');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `emanet`
--

CREATE TABLE `emanet` (
  `emanet_no` int(11) NOT NULL,
  `uye_ID` int(11) NOT NULL,
  `kitap_ISBN` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `kutuphane_ID` int(11) NOT NULL,
  `alım_tarihi` date NOT NULL,
  `teslim_tarihi` date NOT NULL,
  `emanet_durumu` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `emanet`
--

INSERT INTO `emanet` (`emanet_no`, `uye_ID`, `kitap_ISBN`, `kutuphane_ID`, `alım_tarihi`, `teslim_tarihi`, `emanet_durumu`) VALUES
(1, 1, '978-605-106-75-82', 3, '2021-05-30', '2021-06-06', 0),
(2, 1, '978-605-220-50-82', 2, '2021-05-30', '2021-06-06', 0),
(3, 4, '978-605360-35-35', 1, '2021-05-30', '2021-06-06', 0),
(4, 4, '978-605-8301-12-2', 1, '2021-05-30', '2021-06-06', 0);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kategoriler`
--

CREATE TABLE `kategoriler` (
  `id` int(11) NOT NULL,
  `tur` varchar(30) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kategoriler`
--

INSERT INTO `kategoriler` (`id`, `tur`) VALUES
(1, 'Şiir'),
(2, 'Roman'),
(4, 'Cocuk ve Gençlik'),
(5, 'Araştırma-Tarih'),
(6, 'Bilim'),
(7, 'Çizgi Roman'),
(8, 'Din Tasavvuf'),
(9, 'Felsefe'),
(10, 'Kişisel Gelişim');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kitaplar`
--

CREATE TABLE `kitaplar` (
  `ISBN_no_kitap` varchar(45) COLLATE utf8_turkish_ci NOT NULL,
  `kitap_ismi` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `basim_yili` date NOT NULL,
  `kitap_yayınevi` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `kitap_sayisi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kitaplar`
--

INSERT INTO `kitaplar` (`ISBN_no_kitap`, `kitap_ismi`, `basim_yili`, `kitap_yayınevi`, `kitap_sayisi`) VALUES
('978-605-106-75-82', 'ZAMANIN KISA TARİHİ', '2020-12-13', 'Alfa yayınları', 1),
('978-605-220-50-82', '21. YÜZYIL İÇİN 21 DERS', '2018-09-01', 'Kollektif kitap', 1),
('978-605-295-792-3', 'OTOMATİK PORTAKAL', '2019-05-05', 'Türkiye iş bankası kültür yayı', 1),
('978-605-298-08-11', 'KÖRLÜK', '2019-10-11', 'kırmızı kedi yayınevi', 1),
('978-605-311-12-14', 'KUDÜS\'ÜN GİZEMLİ TARİHİ', '2017-05-09', 'Destek yayınları', 1),
('978-605-3650-690', 'KÜÇÜK PRENS', '2017-12-01', 'Can cocuk yayınları', 1),
('978-605-375-60-64', 'WATCHMEN', '2019-05-13', 'ithaki yayınları', 1),
('978-605-384-906-3', 'BEYAZ ZAMBAKLAR ÜLKESİNDE', '2017-07-27', 'yakamaoz kitap', 1),
('978-605-502-93-57', 'SAPIENS', '2017-03-15', 'Kollektif kitap', 1),
('978-605-763-59-83', 'YAKIN TARİHİN GERÇEKLERİ', '2021-03-23', 'Kronik kitap', 1),
('978-605-8301-12-2', 'OSMANLI\'DA DEVLET, HUKUK VE AD', '2020-02-18', 'Kollektif kitap', 0),
('978-605-9144-80-3', 'DÖNÜŞÜM', '2017-01-01', 'İndigo kitap', 1),
('978-605-930-48-01', 'İLK HRISTİYANLAR', '2019-04-04', 'Düşün yayıncılık', 1),
('978-605360-35-35', 'BÖYLE SÖYLEDİ ZERDÜŞT', '2020-07-24', 'Türkiye iş bankası kültür yayı', 0),
('978-625-4050-74-9', 'UYKUSU GELMEYEN PORSUK', '2020-10-20', 'İş bankası kültür yayınları', 1),
('978-975-07-1853-3', '1984', '2019-05-24', 'can sanat yayınları', 1),
('978-975-0803-376', 'BÜYÜK SAAT', '2020-12-10', 'Yapı kredi yayınları', 1),
('978-975-081-38-70', 'GÖĞE BAKMA DURAĞI', '2019-05-13', 'Yapı kredi yayınları', 1),
('978-975-0831-331', 'LAVİNİA', '2019-02-08', 'Yapı kredi yayınları', 1),
('978-975-104-17-53', 'YERALTI ÖYKÜLERİ', '2021-04-19', 'İnkılap kitabevi', 1),
('978-975-3510-25-7', 'TÜRLERİN KÖKENİ', '2009-01-01', 'Onur yayınları', 1),
('978-975-458-71-73', 'DEVLET', '2019-01-30', 'Türkiye iş bankası kültür yayı', 1),
('978-975-6092-16-5', 'CESUR YENİ DÜNYA', '2020-07-01', 'ithaki yayınları', 1);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kitap_kategori`
--

CREATE TABLE `kitap_kategori` (
  `id` int(11) NOT NULL,
  `ISBN_kitap` varchar(45) COLLATE utf8_turkish_ci NOT NULL,
  `id_kategori` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kitap_kategori`
--

INSERT INTO `kitap_kategori` (`id`, `ISBN_kitap`, `id_kategori`) VALUES
(1, '978-605-106-75-82', 6),
(2, '978-605-220-50-82', 5),
(3, '978-605-295-792-3', 2),
(4, '978-605-298-08-11', 2),
(5, '978-605-311-12-14', 8),
(6, '978-605-3650-690', 4),
(7, '978-605-375-60-64', 7),
(8, '978-605-384-906-3', 2),
(9, '978-605-502-93-57', 6),
(10, '978-605-763-59-83', 5),
(11, '978-605-8301-12-2', 5),
(12, '978-605-9144-80-3', 2),
(13, '978-605-930-48-01', 8),
(14, '978-605360-35-35', 9),
(15, '978-625-4050-74-9', 4),
(16, '978-975-07-1853-3', 2),
(17, '978-975-0803-376', 1),
(18, '978-975-081-38-70', 1),
(19, '978-975-0831-331', 1),
(20, '978-975-104-17-53', 7),
(21, '978-975-3510-25-7', 6),
(22, '978-975-458-71-73', 9),
(23, '978-975-6092-16-5', 2);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kitap_kütüphane`
--

CREATE TABLE `kitap_kütüphane` (
  `id` int(11) NOT NULL,
  `ISBN_kitap` varchar(45) COLLATE utf8_turkish_ci NOT NULL,
  `id_kütüphane` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kitap_kütüphane`
--

INSERT INTO `kitap_kütüphane` (`id`, `ISBN_kitap`, `id_kütüphane`) VALUES
(1, '978-605-375-60-64', 2),
(2, '978-975-6092-16-5', 3),
(3, '978-605-295-792-3', 3),
(4, '978-605-3650-690', 1),
(5, '978-975-3510-25-7', 1),
(6, '978-625-4050-74-9', 2),
(7, '978-975-104-17-53', 3),
(8, '978-605-9144-80-3', 3),
(9, '978-605360-35-35', 1),
(10, '978-975-07-1853-3', 3),
(11, '978-605-384-906-3', 2),
(12, '978-605-930-48-01', 1),
(13, '978-605-8301-12-2', 2),
(14, '978-605-763-59-83', 1),
(15, '978-605-298-08-11', 1),
(16, '978-975-0831-331', 3),
(17, '978-605-311-12-14', 3),
(18, '978-975-458-71-73', 2),
(19, '978-605-106-75-82', 1),
(20, '978-975-0803-376', 1),
(21, '978-975-081-38-70', 2),
(22, '978-605-220-50-82', 1),
(23, '978-605-502-93-57', 3);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kitap_yazar`
--

CREATE TABLE `kitap_yazar` (
  `id` int(11) NOT NULL,
  `ISBN_kitap` varchar(45) COLLATE utf8_turkish_ci NOT NULL,
  `id_yazar` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kitap_yazar`
--

INSERT INTO `kitap_yazar` (`id`, `ISBN_kitap`, `id_yazar`) VALUES
(1, '978-605-375-60-64', 1),
(2, '978-975-6092-16-5', 2),
(3, '978-605-295-792-3', 3),
(4, '978-605-3650-690', 4),
(5, '978-975-3510-25-7', 5),
(6, '978-625-4050-74-9', 6),
(7, '978-975-104-17-53', 7),
(8, '978-605-9144-80-3', 8),
(9, '978-605360-35-35', 9),
(10, '978-975-07-1853-3', 10),
(11, '978-605-384-906-3', 11),
(12, '978-605-930-48-01', 12),
(13, '978-605-8301-12-2', 13),
(14, '978-605-763-59-83', 14),
(15, '978-605-298-08-11', 15),
(16, '978-975-0831-331', 16),
(17, '978-605-311-12-14', 17),
(18, '978-975-458-71-73', 18),
(19, '978-605-106-75-82', 19),
(20, '978-975-0803-376', 20),
(21, '978-975-081-38-70', 20),
(22, '978-605-220-50-82', 21),
(23, '978-605-502-93-57', 21);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kütüphaneler`
--

CREATE TABLE `kütüphaneler` (
  `id` int(11) NOT NULL,
  `kütüphane_isim` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `id_adres` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kütüphaneler`
--

INSERT INTO `kütüphaneler` (`id`, `kütüphane_isim`, `id_adres`) VALUES
(1, 'Bursa Şehir Kütüphanesi', 1),
(2, 'Bursa Araştırma Kütüphanesi', 2),
(3, 'Akkılıç Kütüphanesi', 3);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `uye`
--

CREATE TABLE `uye` (
  `ID` int(11) NOT NULL,
  `uye_ad` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `uye_soyad` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `uye_telefon` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `uye_eposta` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `uye_adres` varchar(100) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `uye`
--

INSERT INTO `uye` (`ID`, `uye_ad`, `uye_soyad`, `uye_telefon`, `uye_eposta`, `uye_adres`) VALUES
(1, 'admin', 'tester', '55555', 'admin', 'abcdef'),
(2, 'Zeynep', 'Demirel', '534', 'aaa', 'add'),
(3, 'Melis', 'Varan', '542', 'asdd', 'addd'),
(4, '', '', '', '', ''),
(5, '', '', '', '', ''),
(6, 'deneme', 'deneme', '534', 'deneme', 'adres'),
(7, 'deneme', 'deneme', '534', 'deneme', 'adres');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yazarlar`
--

CREATE TABLE `yazarlar` (
  `id` int(11) NOT NULL,
  `yazar_ad` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `yazar_soyad` varchar(30) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `yazarlar`
--

INSERT INTO `yazarlar` (`id`, `yazar_ad`, `yazar_soyad`) VALUES
(1, 'Alan', 'Moore'),
(2, 'Aldous', 'Huxley'),
(3, 'Anthony', 'Burgess'),
(4, 'Antoine de Saint', 'Exupery'),
(5, 'Charles', 'Darwin'),
(6, 'Constanze Von', 'Kitzing'),
(7, 'Ersin', 'Karabulut'),
(8, 'Franz', 'Kafka'),
(9, 'Friedrich', 'Nietzsche'),
(10, 'George', 'Orwell'),
(11, 'Grigory', 'Petrov'),
(12, 'Hans-Joachim', 'Schoeps'),
(13, 'Halil', 'İnancık'),
(14, 'İlber', 'Ortaylı'),
(15, 'Jose', 'Saramago'),
(16, 'Özdemir', 'Asaf'),
(17, 'Pelin', 'Çift'),
(18, 'Platon', '-'),
(19, 'Stephen', 'Hawking'),
(20, 'Turgut', 'Uyar'),
(21, 'Yuval Noah', 'Harari');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `adresler`
--
ALTER TABLE `adresler`
  ADD PRIMARY KEY (`ID`);

--
-- Tablo için indeksler `emanet`
--
ALTER TABLE `emanet`
  ADD PRIMARY KEY (`emanet_no`),
  ADD KEY `iliski9` (`uye_ID`),
  ADD KEY `iliski16` (`kitap_ISBN`),
  ADD KEY `iliski17` (`kutuphane_ID`);

--
-- Tablo için indeksler `kategoriler`
--
ALTER TABLE `kategoriler`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kitaplar`
--
ALTER TABLE `kitaplar`
  ADD PRIMARY KEY (`ISBN_no_kitap`);

--
-- Tablo için indeksler `kitap_kategori`
--
ALTER TABLE `kitap_kategori`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_kitap_ısbn` (`ISBN_kitap`),
  ADD KEY `fk_id_kategori` (`id_kategori`);

--
-- Tablo için indeksler `kitap_kütüphane`
--
ALTER TABLE `kitap_kütüphane`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ISBN_kitap_fk` (`ISBN_kitap`),
  ADD KEY `fk_kütüphane_id` (`id_kütüphane`);

--
-- Tablo için indeksler `kitap_yazar`
--
ALTER TABLE `kitap_yazar`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_ISBN_kitap` (`ISBN_kitap`),
  ADD KEY `fk_id_yazar` (`id_yazar`);

--
-- Tablo için indeksler `kütüphaneler`
--
ALTER TABLE `kütüphaneler`
  ADD PRIMARY KEY (`id`),
  ADD KEY `iliski15` (`id_adres`);

--
-- Tablo için indeksler `uye`
--
ALTER TABLE `uye`
  ADD PRIMARY KEY (`ID`);

--
-- Tablo için indeksler `yazarlar`
--
ALTER TABLE `yazarlar`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `adresler`
--
ALTER TABLE `adresler`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `emanet`
--
ALTER TABLE `emanet`
  MODIFY `emanet_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Tablo için AUTO_INCREMENT değeri `kategoriler`
--
ALTER TABLE `kategoriler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Tablo için AUTO_INCREMENT değeri `kitap_kategori`
--
ALTER TABLE `kitap_kategori`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Tablo için AUTO_INCREMENT değeri `kitap_kütüphane`
--
ALTER TABLE `kitap_kütüphane`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Tablo için AUTO_INCREMENT değeri `kitap_yazar`
--
ALTER TABLE `kitap_yazar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Tablo için AUTO_INCREMENT değeri `kütüphaneler`
--
ALTER TABLE `kütüphaneler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Tablo için AUTO_INCREMENT değeri `uye`
--
ALTER TABLE `uye`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Tablo için AUTO_INCREMENT değeri `yazarlar`
--
ALTER TABLE `yazarlar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `emanet`
--
ALTER TABLE `emanet`
  ADD CONSTRAINT `iliski16` FOREIGN KEY (`kitap_ISBN`) REFERENCES `kitaplar` (`ISBN_no_kitap`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `iliski17` FOREIGN KEY (`kutuphane_ID`) REFERENCES `kütüphaneler` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `iliski9` FOREIGN KEY (`uye_ID`) REFERENCES `uye` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `kitap_kategori`
--
ALTER TABLE `kitap_kategori`
  ADD CONSTRAINT `fk_id_kategori` FOREIGN KEY (`id_kategori`) REFERENCES `kategoriler` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_kitap_ısbn` FOREIGN KEY (`ISBN_kitap`) REFERENCES `kitaplar` (`ISBN_no_kitap`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `kitap_kütüphane`
--
ALTER TABLE `kitap_kütüphane`
  ADD CONSTRAINT `ISBN_kitap_fk` FOREIGN KEY (`ISBN_kitap`) REFERENCES `kitaplar` (`ISBN_no_kitap`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_kütüphane_id` FOREIGN KEY (`id_kütüphane`) REFERENCES `kütüphaneler` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `kitap_yazar`
--
ALTER TABLE `kitap_yazar`
  ADD CONSTRAINT `fk_ISBN_kitap` FOREIGN KEY (`ISBN_kitap`) REFERENCES `kitaplar` (`ISBN_no_kitap`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_id_yazar` FOREIGN KEY (`id_yazar`) REFERENCES `yazarlar` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `kütüphaneler`
--
ALTER TABLE `kütüphaneler`
  ADD CONSTRAINT `iliski15` FOREIGN KEY (`id_adres`) REFERENCES `adresler` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
