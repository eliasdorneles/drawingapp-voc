import android
from android.widget import LinearLayout, TextView, Button
import android.content.Context
from android.graphics import Bitmap, Canvas, Color, Paint, Path, PorterDuff
from android.view import MotionEvent, Gravity
import android.view

class ButtonClick(implements=android.view.View[OnClickListener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onClick(self, view: android.view.View) -> void:
        self.callback(*self.args, **self.kwargs)

class DrawingView(extends=android.view.View):
    @super({context: android.content.Context})
    def __init__(self, context):
        self.setBackgroundColor(0xfffefefe)
        self.brushSize = 20.0
        self.drawPath = Path()
        self.drawPaint = Paint()
        self.porterDuff = PorterDuff()
        self.canvasPaint = None
        self.paintColor = 0xff55aa00
        self.canvasBitmap = None
        self.drawCanvas = None
        self.setupDrawing()

    def setupDrawing(self):
        self.drawPaint.setColor(self.paintColor)
        self.drawPaint.setAntiAlias(True)
        self.drawPaint.setStrokeWidth(self.brushSize)
        self.drawPaint.setStyle(Paint.Style.STROKE)
        self.drawPaint.setStrokeJoin(Paint.Join.ROUND)
        self.drawPaint.setStrokeCap(Paint.Cap.ROUND)

        self.canvasPaint = Paint(Paint.DITHER_FLAG)

    def onSizeChanged(self, w: int, h: int, oldw: int, oldh: int) -> void:
        print('onSizeChange running')
        # super.onSizeChanged(w, h, oldw, oldh);
        self.canvasBitmap = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888)
        self.drawCanvas = Canvas(self.canvasBitmap)

    def onDraw(self, canvas: android.graphics.Canvas) -> void:
        print('onDraw running')
        canvas.drawBitmap(self.canvasBitmap, 0, 0, self.canvasPaint)
        canvas.drawPath(self.drawPath, self.drawPaint)

    def onTouchEvent(self, event: android.view.MotionEvent) -> bool:
        print('onTouchEvent running')
        touchX = event.getX()
        touchY = event.getY()
        action = event.getAction()
        if action == MotionEvent.ACTION_DOWN:
            self.drawPath.moveTo(touchX, touchY)
        elif action == MotionEvent.ACTION_MOVE:
                self.drawPath.lineTo(touchX, touchY)
        elif action == MotionEvent.ACTION_UP:
                self.drawCanvas.drawPath(self.drawPath, self.drawPaint)
                self.drawPath.reset()
        self.invalidate()
        return True

    def changeColor(self, color: int) -> void:
        print('changing color final step')
        self.paintColor = color
        self.drawPaint.setColor(self.paintColor)

    def change_brushsize(self, size: int) -> void:
        self.brushSize = size
        self.drawPaint.setStrokeWidth(self.brushSize)

    def reset(self) -> void:
        print('reseting')
        self.drawCanvas.drawColor(0, self.porterDuff.Mode.CLEAR)
        self.invalidate()

class MainApp:
    def __init__(self):
        self._activity = android.PythonActivity.setListener(self)

    def onCreate(self):
        drawingView = DrawingView(self._activity)

        hlayout = LinearLayout(self._activity)
        hlayout.setOrientation(LinearLayout.HORIZONTAL)
        hlayout.setGravity(Gravity.CENTER)

        small_brush = Button(self._activity)
        small_brush.setText('Small')
        small_brush.setOnClickListener(ButtonClick(drawingView.change_brushsize, 5.0))
        hlayout.addView(small_brush)

        medium_brush = Button(self._activity)
        medium_brush.setText('Medium')
        medium_brush.setOnClickListener(ButtonClick(drawingView.change_brushsize, 10.0))
        hlayout.addView(medium_brush)

        large_brush = Button(self._activity)
        large_brush.setText('Large')
        large_brush.setOnClickListener(ButtonClick(drawingView.change_brushsize, 20.0))
        hlayout.addView(large_brush)

        reset_button = Button(self._activity)
        reset_button.setText('Reset')
        reset_button.setOnClickListener(ButtonClick(drawingView.reset))
        hlayout.addView(reset_button)

        # colors

        hlayout1 = LinearLayout(self._activity)
        hlayout1.setOrientation(LinearLayout.HORIZONTAL)
        hlayout1.setGravity(Gravity.CENTER)

        red_color = Button(self._activity)
        red_color.setText('Red')
        red_color.getBackground().setColorFilter(0xffff4444, PorterDuff.Mode.MULTIPLY)
        red_color.setOnClickListener(ButtonClick(drawingView.changeColor, 0xffff4444))
        hlayout1.addView(red_color)

        orange_color = Button(self._activity)
        orange_color.setText('Orange')
        orange_color.getBackground().setColorFilter(0xffffBB33, PorterDuff.Mode.MULTIPLY)
        orange_color.setOnClickListener(ButtonClick(drawingView.changeColor, 0xffffBB33))
        hlayout1.addView(orange_color)

        green_color = Button(self._activity)
        green_color.setText('Green')
        green_color.getBackground().setColorFilter(0xff55aa00, PorterDuff.Mode.MULTIPLY)
        green_color.setOnClickListener(ButtonClick(drawingView.changeColor, 0xff55aa00))
        hlayout1.addView(green_color)

        blue_color = Button(self._activity)
        blue_color.setText('Blue')
        blue_color.getBackground().setColorFilter(0xff33b5e5, PorterDuff.Mode.MULTIPLY)
        blue_color.setOnClickListener(ButtonClick(drawingView.changeColor, 0xff33b5e5))
        hlayout1.addView(blue_color)

        vlayout = LinearLayout(self._activity)
        vlayout.setOrientation(LinearLayout.VERTICAL)

        vlayout.addView(hlayout)
        vlayout.addView(hlayout1)
        vlayout.addView(drawingView)

        self._activity.setContentView(vlayout)

def main():
    MainApp()
