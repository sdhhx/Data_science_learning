CREATE DATABASE cnblogsdb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `cnblogsinfo058` (
  `url` char(128) NOT NULL COMMENT 'url链接',
  `title` text COMMENT '标题',
  `summary` text COMMENT '简要概述',
  `id` text  COMMENT '用户id',
  `recommand` int  COMMENT '推荐数',
  `comment` int COMMENT '评论数',
  `view` int COMMENT '浏览数',
  PRIMARY KEY (`url`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;