# Code update hồ sơ tổ QC
 #   C o d e  đổi tên  f i l e   t h e o   f o l d e r 

 i m p o r t   o s , o s . p a t h   # U P D A T E   O S 
 i m p o r t   f n m a t c h 
 i m p o r t   d a t e t i m e 
 i m p o r t   t i m e 
 f r o m   d a t e t i m e   i m p o r t   d a t e 
 i m p o r t   p a n d a s   a s   p d 
 i m p o r t   g l o b 
 d e f   e m _ m i n h ( ) : 
         s t a r t _ p a t h   =   " " " D : / C H U Y E N   K H A C   T R O N G   N G A Y / N A M   2 0 1 8 / T H A N G   6 - 2 0 1 8 / " " "   #Chỉnh sửa thông tin
         e x t r a c t e d _ f o l d e r   =   [ n a m e   f o r   n a m e   i n   o s . l i s t d i r ( s t a r t _ p a t h )   i f   o s . p a t h . i s d i r ( o s . p a t h . j o i n ( s t a r t _ p a t h ,   n a m e ) ) ] 
         e m _ m i n h _ d a t e   =   d a t e t i m e . d a t e t i m e . t o d a y ( ) . s t r f t i m e ( ' % d - % m - % y - % H - % M ' ) 
         s t a r t _ n u m   =   1 
 # Sửa thông tin12
         f o r   n e w _   i n   e x t r a c t e d _ f o l d e r : 
                 o s . c h d i r ( o s . p a t h . j o i n ( s t a r t _ p a t h , n e w _ ) ) 
                 b   =   o s . g e t c w d ( ) 
                 e x t r a c t e d _ f o l d e r   =   [ n a m e   f o r   n a m e   i n   o s . l i s t d i r ( b )   i f   o s . p a t h . i s d i r ( o s . p a t h . j o i n ( b ,   n a m e ) ) ] 
 
                 f o r   n e w _   i n   e x t r a c t e d _ f o l d e r : 
 
                         i f   f n m a t c h . f n m a t c h ( n e w _ , ' * - * - * - * ' ) : 
 
                                 o s . c h d i r ( o s . p a t h . j o i n ( b , n e w _ ) ) 
                                 o r d e r _ i d   =   n e w _ . s p l i t ( ' - ' ) [ : 3 ] 
                                 o r d e r _ i d   =   ' - ' . j o i n ( o r d e r _ i d ) 
                                 o r d e r _ n a m e   =   n e w _ . s p l i t ( ' - ' ) [ 3 ] . s p l i t ( ) [ 0 ] 
 
                                 f o r   e m _ m i n h   i n   o s . l i s t d i r ( ) : 
                                         i f   f n m a t c h . f n m a t c h ( e m _ m i n h , ' I M G _ * . J P G ' )   o r   f n m a t c h . f n m a t c h ( e m _ m i n h , ' * [ 0 - 9 ] . J P G ' )   o r   f n m a t c h . f n m a t c h ( e m _ m i n h , ' I M G _ * . j p g ' )   o r   f n m a t c h . f n m a t c h ( e m _ m i n h , ' * [ 0 - 9 ] . j p g ' ) : 
                                                 f i l e _ e x t   =   e m _ m i n h . r p a r t i t i o n ( " . " ) [ - 1 ] 
                                                 o s . r e n a m e ( e m _ m i n h , f ' { o r d e r _ i d } - { o r d e r _ n a m e }   -   { e m _ m i n h _ d a t e }   -   h s - { s t a r t _ n u m } - . { f i l e _ e x t } '   ) 
                                                 s t a r t _ n u m   + = 1 
                                 s t a r t _ n u m   =   1 
                         e l s e : 
                                 i f   f n m a t c h . f n m a t c h ( n e w _ , ' * - * ' ) : 
                                         o s . c h d i r ( o s . p a t h . j o i n ( b , n e w _ ) ) 
                                         o r d e r _ i d   =   s t r ( n e w _ . s p l i t ( ' - ' ) [ 0 ] ) . u p p e r ( ) 
                                         o r d e r _ n a m e   =   s t r ( n e w _ . s p l i t ( ' - ' ) [ 1 ] . s p l i t ( ) [ 0 ] ) . u p p e r ( ) 
                                         f o r   e m _ m i n h   i n   o s . l i s t d i r ( ) : 
                                                 i f   f n m a t c h . f n m a t c h ( e m _ m i n h , ' I M G _ * . J P G ' )   o r   f n m a t c h . f n m a t c h ( e m _ m i n h , ' [ 0 - 9 ] * . J P G ' )   o r   f n m a t c h . f n m a t c h ( e m _ m i n h , ' I M G _ * . j p g ' )   o r   f n m a t c h . f n m a t c h ( e m _ m i n h , ' [ 0 - 9 ] * . j p g ' ) : 
                                                         f i l e _ e x t   =   e m _ m i n h . r p a r t i t i o n ( " . " ) [ - 1 ] 
                                                         o s . r e n a m e ( e m _ m i n h , f ' { o r d e r _ i d } - { o r d e r _ n a m e }   -   { e m _ m i n h _ d a t e }   -   h s - { s t a r t _ n u m } . { f i l e _ e x t } '   ) 
                                                         s t a r t _ n u m   + = 1 
                                         s t a r t _ n u m   =   1 
         p r i n t ( f ' X o n g :   { e m _ m i n h _ d a t e } ' ) 
 
 w h i l e   T r u e : 
         t r y : 
                 e m _ m i n h ( ) 
                 t i m e . s l e e p ( 1 5 ) 
         e x c e p t : 
                 p a s s 
 
