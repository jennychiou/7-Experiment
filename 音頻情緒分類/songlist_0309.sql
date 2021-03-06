-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1:3306
-- 產生時間： 2019-03-07 13:11:28
-- 伺服器版本: 5.7.21
-- PHP 版本： 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `nchu`
--

-- --------------------------------------------------------

--
-- 資料表結構 `songlist`
--

DROP TABLE IF EXISTS `songlist`;
CREATE TABLE IF NOT EXISTS `songlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `song` varchar(200) NOT NULL,
  `singer` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=501 DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `songlist`
--

INSERT INTO `songlist` (`id`, `song`, `singer`) VALUES
(1, '1979', 'Smashing Pumpkins'),
(2, '1-800-273-8255', 'Logic'),
(3, '24K Magic', 'Bruno Mars'),
(4, '7 rings', 'Ariana Grande'),
(5, 'A Million Dreams', 'Ziv Zaifman'),
(6, 'A Thousand Years', 'Christina Perri'),
(7, 'Acamar', 'Frankey'),
(8, 'Accelerate', 'Jungle'),
(9, 'Accidentally In Love', 'Counting Crows'),
(10, 'Affection', 'Crystal Castles'),
(11, 'Ahora Dice', 'Chris Jeday'),
(12, 'Ain\'t No Love In The Heart Of The City - Single Version', 'Bobby "Blue" Bland'),
(13, 'All Day', 'Kanye West'),
(14, 'All Day And All Of The Night', 'The Kinks'),
(15, 'All I Need', 'Tim Halperin'),
(16, 'All Night', 'The Vamps'),
(17, 'All of Me', 'John Legend'),
(18, 'All of the Stars', 'Ed Sheeran'),
(19, 'All These Things That I\'ve Done', 'The Killers'),
(20, 'Alone', 'Alan Walker'),
(21, 'Alright', 'Kendrick Lamar'),
(22, 'Always Be My Baby', 'Tim Halperin'),
(23, 'Always Remember Us This Way', 'Lady Gaga'),
(24, 'Amazing', 'Westlife'),
(25, 'Amsterdam', 'Coldplay'),
(26, 'Annie', 'Neon Indian'),
(27, 'Anything New', 'Bibio'),
(28, 'Attention', 'Charlie Puth'),
(29, 'Awake', 'Tycho'),
(30, 'Bad and Boujee (feat. Lil Uzi Vert)', 'Migos'),
(31, 'bad idea', 'Ariana Grande'),
(32, 'Bad Liar', 'Imagine Dragons'),
(33, 'Bad Things', 'Machine Gun Kelly'),
(34, 'Bam Bam', 'Sister Nancy'),
(35, 'Bang That', 'Disclosure'),
(36, 'Bang! Bang!', 'Joe Cuba'),
(37, 'Bank Account', '21 Savage'),
(38, 'Be A Body', 'Grimes'),
(39, 'Be Alright', 'Dean Lewis'),
(40, 'Be My Baby', 'The Ronettes'),
(41, 'Beach House', 'The Chainsmokers'),
(42, 'Believer', 'Imagine Dragons'),
(43, 'Best Friend', 'Young Thug'),
(44, 'Better', 'Khalid'),
(45, 'Better Man', 'Little Big Town'),
(46, 'Better Now', 'Post Malone'),
(47, 'Better Than Today', 'Rhys Lewis'),
(48, 'Big Plans', "Why Don't We"),
(49, 'Big Rings', 'Drake'),
(50, 'Billie Holiday', 'Warpaint'),
(51, 'Binge', 'Papa Roach'),
(52, 'Black Mags', 'The Cool Kids'),
(53, 'Black Out Days', 'Phantogram'),
(54, 'Bless My Soul', 'Nightmares On Wax'),
(55, 'Blood On The Leaves', 'Kanye West'),
(56, 'Blood On the Money', 'Future'),
(57, 'Body Like A Back Road', 'Sam Hunt'),
(58, 'Bounce Back', 'Big Sean'),
(59, 'Bouncin', 'Chief Keef'),
(60, 'Bruises', 'Lewis Capaldi'),
(61, 'Burn', 'Nine Inch Nails'),
(62, 'bury a friend', 'Billie Eilish'),
(63, 'California Nights', 'Best Coast'),
(64, 'Candy Cane Lane', 'Sia'),
(65, 'Capitol', 'TR/ST'),
(66, 'Careless', 'Dusky'),
(67, 'Castle on the Hill', 'Ed Sheeran'),
(68, 'Cemalim', 'Erkin Koray'),
(69, 'Chained To The Rhythm', 'Katy Perry'),
(70, 'Chances', 'Backstreet Boys'),
(71, 'Chandelier', 'Sia'),
(72, 'Changes', 'Chris Lake '),
(73, 'Chantaje', 'Shakira'),
(74, 'Char', 'Crystal Castles'),
(75, 'Chasing Heaven', 'Bassnectar'),
(76, 'Check', 'Young Thug'),
(77, 'Childs Play', 'Drake'),
(78, 'Chlorine', 'Twenty One Pilots'),
(79, 'Closer', 'The Chainsmokers'),
(80, 'Cocaine Model', 'ZHU'),
(81, 'Cold', 'Maroon 5'),
(82, 'Cold In LA', "Why Don't We"),
(83, 'Cold Water', 'Major Lazer'),
(84, 'Colors And The Kids', 'Cat Power'),
(85, 'Come Save Me', 'Jagwar Ma'),
(86, 'comethru', 'Jeremy Zucker'),
(87, 'Coming Home', 'Leon Bridges'),
(88, 'Confess To Me', 'Disclosure'),
(89, 'Congratulations', 'Post Malone'),
(90, 'Counting', 'Autre Ne Veut'),
(91, 'Crosstown Traffic', 'Jimi Hendrix'),
(92, 'Cry Like A Ghost', 'Passion Pit'),
(93, 'Danger and Dread', 'Brown Bird'),
(94, 'Dark Matter', 'Feathers'),
(95, 'Delicate', 'Taylor Swift'),
(96, 'Demon', 'Shamir'),
(97, 'Digital Animal', 'Honey Claws'),
(98, 'DNA.', 'Kendrick Lamar'),
(99, 'Don\'t Call Me Up', 'Mabel'),
(100, 'Don\'t Let Me Down', 'The Chainsmokers'),
(101, 'Don\'t Miss', 'The Alexanders'),
(102, 'Don\'t Move', 'Phantogram'),
(103, 'Don\'t Wanna Know', 'Maroon 5'),
(104, 'Don\'t You Evah', 'Spoon'),
(105, 'Dopeman', 'Vince Staples'),
(106, 'Double Bubble Trouble', 'M.I.A.'),
(107, 'Dry', 'PJ Harvey'),
(108, 'Dusk Till Dawn', 'ZAYN'),
(109, 'El Amante', 'Nicky Jam'),
(110, 'Electioneering', 'Radiohead'),
(111, 'Elizabeth on the Bathroom Floor', 'Eels'),
(112, 'Endless Rhythm', 'Baio'),
(113, 'Estrelar', 'Marcos Valle'),
(114, 'Every 1\'s A Winner', 'Hot Chocolate'),
(115, 'Everybody Likes Something Good', 'Ify Jerry Crusade'),
(116, 'Evil Friends (feat. Danny Brown)', 'Portugal. The Man'),
(117, 'Faded', 'Alan Walker'),
(118, 'Fail to Cry', 'Yacht Club'),
(119, 'Fake Love', 'Drake'),
(120, 'Fake Tales Of San Francisco', 'Arctic Monkeys'),
(121, 'Fall In Love', 'Phantogram'),
(122, 'Falling Slowly', 'Glen Hansard'),
(123, 'Fantastic Man', 'William Onyeabor'),
(124, 'Feels', 'Calvin Harris'),
(125, 'Felices los 4', 'Maluma'),
(126, 'Fire', 'Sara Bareilles'),
(127, 'Fire And Rain', 'James Taylor'),
(128, 'Flashlight', 'Parliament'),
(129, 'FOOLISH', 'Meghan Trainor'),
(130, 'Forever', 'Majid Jordan'),
(131, 'Free Stress Test', 'Professor Murder'),
(132, 'Friends', 'Justin Bieber'),
(133, 'From Now On', 'Hugh Jackman'),
(134, 'Galway Girl', 'Ed Sheeran'),
(135, 'Get Away', 'CHVRCHES'),
(136, 'Girlfriend', 'Ty Segall'),
(137, 'Give in To Me', 'Lika Morgan'),
(138, 'Glad I Met You', 'D. Gookin'),
(139, 'Glorious', 'Macklemore'),
(140, 'Go', 'Grimes'),
(141, 'God is a woman', 'Ariana Grande'),
(142, 'GodLovesUgly', 'Atmosphere'),
(143, 'Gold and a Pager', 'The Cool Kids'),
(144, 'Good Mistake', 'Mr Little Jeans'),
(145, 'Good Years', 'ZAYN'),
(146, 'Goody Two Shoes', 'Duck Sauce'),
(147, 'goosebumps', 'Travis Scott'),
(148, 'Hannah Montana', 'Migos'),
(149, 'Havana', 'Camila Cabello'),
(150, 'Have Love Will Travel', 'The Sonics'),
(151, 'Hazelton Trump', 'OB OBrien'),
(152, 'Head Above Water', 'Avril Lavigne'),
(153, 'Heal Me', 'Lady Gaga'),
(154, 'Hear Me Now', 'Alok'),
(155, 'Heaven And Hell Is On Earth', '20th Century Steel Band'),
(156, 'Hello My Love', 'Westlife'),
(157, 'Hello My Love', 'Westlife'),
(158, 'Her Fantasy', 'Matthew Dear'),
(159, 'Hercules', 'Young Thug'),
(160, 'Hercules Theme', 'Hercules & Love Affair'),
(161, 'Hero', 'Mariah Carey'),
(162, 'High School Lover', 'Cayucas'),
(163, 'Hit the Road Jack', 'Ray Charles'),
(164, 'Ho Ho Ho', 'Sia'),
(165, 'Hold My Girl', 'George Ezra'),
(166, 'Hold On We\'re Going Home', 'ASTR'),
(167, 'Hot Blur', 'How Sad'),
(168, 'Hot Dreams', 'Timber Timbre'),
(169, 'Hotline Bling', 'Drake'),
(170, 'House of Jealous Lovers', 'The Rapture'),
(171, 'How Did I Get Here', 'ODESZA'),
(172, 'How Do I Live', 'Trisha Yearwood'),
(173, 'How Far I\'ll Go', 'Alessia Cara'),
(174, 'How Long Will I Love You', 'Ellie Goulding'),
(175, 'I Ain\'t Trippin off Nothin', 'Ezale'),
(176, 'I Don\'t Know What Love Is', 'Lady Gaga'),
(177, 'I Don\'t Sell Molly No More', 'ILoveMakonnen'),
(178, 'I Feel It Coming', 'The Weeknd'),
(179, 'I Guess I Just Feel Like', 'John Mayer'),
(180, 'I Had A Dream', 'Kelly Clarkson'),
(181, 'I Know There\'s Gonna Be', 'Jamie xx'),
(182, 'I Like Me Better', 'Lauv'),
(183, 'I Like The Way', 'Against The Current'),
(184, 'I Miss You', 'Clean Bandit'),
(185, 'I Need To Wake Up', 'Melissa Etheridge'),
(186, 'I Shall Be Released', 'Nina Simone'),
(187, 'I Will Always Love You', 'Whitney Houston'),
(188, 'I Wish', 'Stevie Wonder'),
(189, 'I Would Die 4 U', 'Prince'),
(190, 'If I Gave You My Love', 'Myron & E'),
(191, 'If The World Ends', 'Guillemots'),
(192, 'Ikimiz Bir Fidaniz', 'Umit Aksu Orkestrasi'),
(193, 'I\'Ll Do Anything', 'Courtney Love'),
(194, 'I\'m a Mess', 'Bebe Rexha'),
(195, 'I\'m Already There', 'Westlife'),
(196, 'I\'m In Love', 'Fool\'s Gold'),
(197, 'I\'m the One', 'DJ Khaled'),
(198, 'I\'m Ya Dogg', 'Snoop Dogg'),
(199, 'imagine', 'Ariana Grande'),
(200, 'Imma Ride', 'Young Thug'),
(201, 'Immortals', 'Fall Out Boy'),
(202, 'In My Blood', 'Shawn Mendes'),
(203, 'In My Feelings', 'Drake'),
(204, 'In the End', 'Family of the Year'),
(205, 'In the Name of Love', 'Martin Garrix'),
(206, 'Inspector Norse', 'Todd Terje'),
(207, 'Interlude', 'Alan Walker'),
(208, 'International Players Anthem', 'Swishahouse'),
(209, 'Intro', 'Alan Walker'),
(210, 'Is That Alright?', 'Lady Gaga'),
(211, 'Issues', 'Julia Michaels'),
(212, 'Issues', 'Julia Michaels'),
(213, 'It All Feels Right', 'Washed Out'),
(214, 'It Looks Like Love', 'Goody Goody'),
(215, 'It\'s My Party', 'Lesley Gore'),
(216, 'I\'ve Seen Footage', 'Death Grips'),
(217, 'Jumpman', 'Drake'),
(218, 'Junk of the Heart', 'The Kooks'),
(219, 'Just Hold On', 'Steve Aoki'),
(220, 'Killer Queen', '5 Seconds of Summer'),
(221, 'Kiss From A Rose', 'Seal'),
(222, 'Kiss Me', 'Sixpence None The Richer'),
(223, 'Know Yourself', 'Drake'),
(224, 'Last Chance to Dance', 'Ekkah'),
(225, 'Last Hurrah', 'Bebe Rexha'),
(226, 'Leave A Trace', 'CHVRCHES'),
(227, 'Leave House', 'Caribou'),
(228, 'Let It Happen', 'Tame Impala'),
(229, 'Let Me Down Slowly', 'Alec Benjamin'),
(230, 'Let Me Love You', 'DJ Snake'),
(231, 'Let Me Show You Love', 'Cut Copy'),
(232, 'Let You Love Me', 'Rita Ora'),
(233, 'Lie for Love', 'Sabrina Carpenter'),
(234, 'Light House', 'Future Islands'),
(235, 'Light Up', 'Tim Halperin'),
(236, 'Little People (Black City)', 'Matthew Dear'),
(237, 'Location', 'Khalid'),
(238, 'Look Alive', 'Rae Sremmurd'),
(239, 'Look At Wrist', 'Father'),
(240, 'Look at You', 'George McCrae'),
(241, 'Look Back At It', 'A Boogie Wit da Hoodie'),
(242, 'Look What I Found', 'Lady Gaga'),
(243, 'Look What You Made Me Do', 'Taylor Swift'),
(244, 'Lose My Mind', 'A-Trak'),
(245, 'Losing You', 'Solange'),
(246, 'Lost In Japan', 'Shawn Mendes'),
(247, 'Lost In The Fire', 'Four of Diamonds'),
(248, 'Lost Stars', 'Adam Levine'),
(249, 'Lost You', 'Zeds Dead'),
(250, 'Loud Places', 'Jamie xx'),
(251, 'Love Me Again', 'John Newman'),
(252, 'Love Sosa', 'Chief Keef'),
(253, 'Lovefool', 'The Cardigans'),
(254, 'Magnets', 'Disclosure'),
(255, 'Magnolia', 'Young & Sick'),
(256, 'Malibu', 'Miley Cyrus'),
(257, 'Mama', 'Jonas Blue'),
(258, 'Mandy', 'Westlife'),
(259, 'Maneuvering', 'ILoveMakonnen'),
(260, 'Marijuana', 'Chrome Sparks'),
(261, 'Mask Off', 'Future'),
(262, 'Master Of None', 'Beach House'),
(263, "Maybe It's Time", 'Bradley Cooper'),
(264, 'medicine', 'Bring Me The Horizon'),
(265, 'Mercy', 'Kanye West'),
(266, 'Mi Gente', 'J Balvin'),
(267, 'Midnight City', 'M83'),
(268, 'Milly Rock', '2milly'),
(269, 'Missed', 'PJ Harvey'),
(270, 'Monster', 'Kanye West'),
(271, 'More Than That', 'Lauren Jauregui'),
(272, 'More Than You Know', 'Axwell /\\ Ingrosso'),
(273, 'Moving to the Left', 'Woods'),
(274, 'Music To My Eyes', 'Lady Gaga'),
(275, 'My Brain Tells My Body', 'The Vandals'),
(276, 'My Sundown', 'Jimmy Eat World'),
(277, 'Natural', 'Imagine Dragons'),
(278, 'Need to Know', 'Calum Scott'),
(279, 'Nervous', 'Shawn Mendes'),
(280, 'Never Enough', 'Loren Allred'),
(281, 'Never Had A Dream Come True', 'S Club 7'),
(282, 'Never Say Never', 'The Fray'),
(283, 'New', 'Daya'),
(284, 'New Rules', 'Dua Lipa'),
(285, 'New Slaves', 'Kanye West'),
(286, 'New York City', 'Christopher Owens'),
(287, 'Next to You', 'Poolside'),
(288, 'No Place', 'Backstreet Boys'),
(289, 'No Promises', 'Cheat Codes'),
(290, 'No Rest For The Wicked', 'Lykke Li'),
(291, 'no tears left to cry', 'Ariana Grande'),
(292, 'No Type', 'Rae Sremmurd'),
(293, 'Not About Angels', 'Birdy'),
(294, 'Nothing Ever Happened', 'Deerhunter'),
(295, 'Now Or Never', 'Halsey'),
(296, 'Oh My Darling Don\'t Meow (Just Blaze Remix)', 'Run The Jewels'),
(297, 'Okay', 'Holy Ghost!'),
(298, 'One Dance', 'Drake'),
(299, 'One Fine Day', 'The Chiffons'),
(300, 'One More Chance', 'James Collins'),
(301, 'One Nation Under a Groove', 'Funkadelic'),
(302, 'One Night', 'Lil Yachty'),
(303, 'Operate', 'ASTR'),
(304, 'Our Love', 'Caribou'),
(305, 'Paperthin Hymn', 'Anberlin'),
(306, 'Papi Pacify', 'FKA twigs'),
(307, 'Paris', 'The Chainsmokers'),
(308, 'Pass The Dutchie', 'Musical Youth'),
(309, 'Passionfruit', 'Drake'),
(310, 'Passionfruit', 'Drake'),
(311, 'Perfect', 'Ed Sheeran'),
(312, 'Pick Up The Pieces', 'Average White Band'),
(313, 'Platoon', 'Jungle'),
(314, 'Please Mr. Postman', 'The Marvelettes'),
(315, 'Please Stop Making Fake Versace', 'Father'),
(316, 'Poppin\' My Collar', 'Three 6 Mafia'),
(317, 'Preach', 'John Legend'),
(318, 'Preach', 'John Legend'),
(319, 'Pretty Girl', 'Maggie Lindemann'),
(320, 'Pussy', 'Brazilian Girls'),
(321, 'Pyramids', 'Frank Ocean'),
(322, 'Queen\'s Speech 4', 'Lady Leshurr'),
(323, 'Rainy Streets', 'Blue In Green'),
(324, 'Raise A Man', 'Alicia Keys'),
(325, 'Redbone', 'Childish Gambino'),
(326, 'Redbone', 'Childish Gambino'),
(327, 'Reminiscing', 'Little River Band'),
(328, 'Return Of The Mack - C & J Street Mix', 'Mark Morrison'),
(329, 'Rewind', 'Kelela'),
(330, 'Rewrite The Stars', 'Zac Efron'),
(331, 'Right Place Wrong Time', 'Dr. John'),
(332, 'Rill Rill', 'Sleigh Bells'),
(333, 'River', 'Ibeyi'),
(334, 'River', 'Leon Bridges'),
(335, 'rockstar', 'Post Malone'),
(336, 'Ruin My Life', 'Zara Larsson'),
(337, 'Sabali', 'Amadou & Mariam'),
(338, 'San Francisco', 'Foxygen'),
(339, 'Sanctified', 'Rick Ross'),
(340, 'Saturday Love', 'Toro y Moi'),
(341, 'Saturday Nights', 'Khalid'),
(342, 'Say You Won\'t Let Go', 'James Arthur'),
(343, 'Scared to Be Lonely', 'Martin Garrix'),
(344, 'Seasons in the Sun', 'Westlife'),
(345, 'See Blind Through', 'Canyons'),
(346, 'Sentimental Trash', 'Sweet Valley'),
(347, 'Sexy Socialite', 'Chromeo'),
(348, 'Shallow', 'Lady Gaga'),
(349, 'Shape of You', 'Ed Sheeran'),
(350, 'She', 'Elvis Costello'),
(351, 'Shotgun', 'George Ezra'),
(352, 'Side To Side', 'Ariana Grande'),
(353, 'Sign of the Times', 'Harry Styles'),
(354, 'Silence', 'Marshmello'),
(355, 'Skyfall', 'Adele'),
(356, 'Slide', 'Calvin Harris'),
(357, 'Slow Hands', 'Niall Horan'),
(358, 'Slumlord', 'Neon Indian'),
(359, 'Smell Yo D*ck', 'Riskay'),
(360, 'SOLO', 'JENNIE'),
(361, 'Solo Dance', 'Martin Jensen'),
(362, 'Somebody\'s Watching Me', 'Rockwell'),
(363, 'Someone You Loved', 'Lewis Capaldi'),
(364, 'Something Just Like This', 'The Chainsmokers'),
(365, 'Something Left To Give', 'The Starting Line'),
(366, 'Sometimes', 'Heems'),
(367, 'Somewhere Only We Know', 'Keane'),
(368, 'Sorry Not Sorry', 'Demi Lovato'),
(369, 'Speakerbox', 'Bassnectar'),
(370, 'Spill The Wine', 'Eric Burdon'),
(371, 'Spooky', 'Dusty Springfield'),
(372, 'Starboy', 'The Weeknd'),
(373, 'Started From the Bottom', 'Drake'),
(374, 'Starving', 'Hailee Steinfeld'),
(375, 'Stay', 'Post Malone'),
(376, 'Stay With Me', 'CHANYEOL'),
(377, 'Stray', 'Grace VanderWaal'),
(378, 'Strip Me', 'Natasha Bedingfield'),
(379, 'Strip That Down', 'Liam Payne'),
(380, 'Strychnine', 'The Sonics'),
(381, 'SUBEME LA RADIO', 'Enrique Iglesias'),
(382, 'Subways', 'The Avalanches'),
(383, 'Suddenly I See', 'KT Tunstall'),
(384, 'Sugar', 'Maroon 5'),
(385, 'Sugar for the Queen', 'Bells Atlas'),
(386, 'Summer Madness', 'Kool & The Gang'),
(387, 'Sun In The Night', 'Lighthouse Family'),
(388, 'Sunflower', 'Stanaj'),
(389, 'Sunshine Of Your Love', 'Cream'),
(390, 'Sweater Weather', 'The Neighbourhood'),
(391, 'Swerve', 'ILoveMakonnen'),
(392, 'Symphony', 'Clean Bandit'),
(393, 'Take You On', 'Peaches'),
(394, 'Talk About', 'Les Sins'),
(395, 'That\'s What I Like', 'Bruno Mars'),
(396, 'The Buzz (feat. Mataya & Young Tapz)', 'Hermitude'),
(397, 'The Chase', 'Future Islands'),
(398, 'The Cure', 'Lady Gaga'),
(399, 'The Diary Of Jane', 'Breaking Benjamin'),
(400, 'The Gaudy Side of Town', 'Gayngs'),
(401, 'The Greatest Show', 'Hugh Jackman'),
(402, 'The Hills', 'The Weeknd'),
(403, 'The Incidentals', "Alisha's Attic"),
(404, 'The Magnificent Seven - Remastered', 'The Clash'),
(405, 'The Other Side', 'Hugh Jackman'),
(406, 'The Payback', 'James Brown'),
(407, 'The Righteous One', 'The Orwells'),
(408, 'The River', 'Son Little'),
(409, 'The Rose', 'Westlife'),
(410, 'The Show', 'Lenka'),
(411, 'The Wire', 'HAIM'),
(412, 'Then He Kissed Me', 'The Crystals'),
(413, 'There for You', 'Martin Garrix'),
(414, 'There You Are', 'ZAYN'),
(415, 'There\'s Nothing Holdin\' Me Back', 'Shawn Mendes'),
(416, 'They Come in Gold', 'Shabazz Palaces'),
(417, 'They Don\'t Know - Original Mix', 'Disciples'),
(418, 'This Is America', 'Childish Gambino'),
(419, 'This Is Me', 'Keala Settle'),
(420, 'This Ready Flesh', 'TR/ST'),
(421, 'This Time Around', 'Softwar'),
(422, 'Thunder', 'Imagine Dragons'),
(423, 'Tides of Neptune', 'Virgo'),
(424, 'Tightrope', 'Michelle Williams'),
(425, 'Tiny Dancer', 'Elton John'),
(426, 'Tired', 'Alan Walker'),
(427, 'To The Top', 'Twin Shadow'),
(428, 'Too Far Gone', 'Bradley Cooper'),
(429, 'Too Good At Goodbyes', 'Sam Smith'),
(430, 'Town Called Malice', 'The Jam'),
(431, 'Traffic', 'Lil Reese'),
(432, 'Trap Queen', 'Fetty Wap'),
(433, 'Trill Hoe', 'Western Tink'),
(434, 'Trust Me Danny', 'ILoveMakonnen'),
(435, 'Trust My Lonely', 'Alessia Cara'),
(436, 'Tuesday', 'ILoveMakonnen'),
(437, 'U Mad', 'Vic Mensa'),
(438, 'Unbound', 'Cathedrals'),
(439, 'Uncast Shadow Of A Southern Myth', 'Parquet Courts'),
(440, 'Uncle ACE', 'Blood Orange'),
(441, 'Undecided', 'Chris Brown'),
(442, 'Unforgettable', 'French Montana'),
(443, 'Upper Echelon', 'Travis Scott'),
(444, 'Versace Python', 'Riff Raff'),
(445, 'Voices', 'Against The Current'),
(446, 'Wait for the Man', 'FIDLAR'),
(447, 'Walk', 'Kwabs'),
(448, 'Walk Me Home', 'P!nk'),
(449, 'Walking Into Sunshine', 'Central Line'),
(450, 'Watching You', 'Melissa Etheridge'),
(451, 'Water No Get Enemy', 'Fela Kuti'),
(452, 'We All Need Saving', 'The Eight Tracks'),
(453, 'We Exist', 'Arcade Fire'),
(454, 'We Sleep In The Ocean', 'The Cloud Room'),
(455, 'Weak', 'AJR'),
(456, 'Weight', 'Mikal Cronin'),
(457, 'What About Now', 'Westlife'),
(458, 'What About Us', 'P!nk'),
(459, 'What I Miss Most', 'Calum Scott'),
(460, 'What I\'ve Done', 'Linkin Park'),
(461, 'When I Fall In Love', 'Celine Dion'),
(462, 'When The Night Falls', 'Chromeo'),
(463, 'When They Fight'  ' They Fight', 'Generationals'),
(464, 'When You Say Nothing At All', 'Boyzone'),
(465, 'White Girl', 'Shy Glizzy'),
(466, 'White Iverson', 'Post Malone'),
(467, 'Who Be Lovin Me', 'Santigold'),
(468, 'Why Don\'t They Let Us Fall in Love', 'The Ronettes'),
(469, 'Wild Thoughts', 'DJ Khaled'),
(470, 'Will You Love Me Tomorrow', 'The Shirelles'),
(471, 'Willing & Able', 'Disclosure'),
(472, 'Wishes', 'Beach House'),
(473, 'With That', 'Young Thug'),
(474, 'With You', 'Mariah Carey'),
(475, 'Without Me', 'Halsey'),
(476, 'Wolves', 'Selena Gomez'),
(477, 'Words I Don\'t Remember', 'How To Dress Well'),
(478, 'World In Motion', 'New Order'),
(479, 'Xanny Family', 'Future'),
(480, 'You Don\'t Know Me', 'Jax Jones'),
(481, 'You Raise Me Up', 'Westlife'),
(482, 'Young Dumb & Broke', 'Khalid'),
(483, 'Youngblood', '5 Seconds of Summer'),
(484, 'Your Song', 'Rita Ora'),
(485, 'You\'re Not Good Enough', 'Blood Orange'),
(486, 'You\'re the Best', 'Wet'),
(487, 'Flying Without Wings', 'Westlife'),
(488, 'Us Against the World', 'Westlife'),
(489, 'More than Words', 'Westlife'),
(490, 'Worth It', 'YK Osiris'),
(491, 'Payphone', 'Maroon 5'),
(492, 'This Love', 'Maroon 5'),
(493, 'Animals', 'Maroon 5'),
(494, 'Maps', 'Maroon 5'),
(495, 'Makes Me Wonder', 'Maroon 5'),
(496, 'Feelings', 'Maroon 5'),
(497, 'It Was Always You', 'Maroon 5'),
(498, 'Closure', 'Maroon 5'),
(499, 'Just A Feeling', 'Maroon 5'),
(500, 'One More Night', 'Maroon 5');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
