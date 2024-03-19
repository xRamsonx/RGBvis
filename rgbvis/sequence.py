from rgbvis.section import Section
from plotly.subplots import make_subplots
import plotly.graph_objects as go

class Sequence:
    def __init__(self):
        self.sequence = [[],[],[]] # red, green, blue
    
    def add(self, type, duration, endvalue, rgbs="rgb", intensity=1.0):
        if "r" in rgbs.lower():
            self.sequence[0].append([duration,Section(type, endvalue, intensity)])	
        if "g" in rgbs.lower():
            self.sequence[1].append([duration,Section(type, endvalue, intensity)])
        if "b" in rgbs.lower():
            self.sequence[2].append([duration,Section(type, endvalue, intensity)])
    
    def evaluate(self, time):
        rgb = [0,0,0]
        total_time = time
        for i in range(3):
            endval = 0
            time = total_time
            for duration, section in self.sequence[i]:
                # Check which section is currently active and evaluate it
                if time > duration: 
                    endval = section.endvalue
                    time -= duration
                else:
                    # Normalize time to 0-1 to simplify calculations
                    eval_time = time/duration
                    # Evaluate the section and normalize the result to the endvalue
                    rgb[i] = endval + section.evaluate(eval_time)*(section.endvalue-endval)
                    break
                rgb[i] = 0
        return tuple(rgb)

    def get_values(self, x):
        y = []
        for i in x:
            y.append(self.evaluate(i))
        return y
    
    def lines(self, x):
        y = self.get_values(x)
        return [go.Scatter(x=x, y=[i[color] for i in y], mode='lines', 
                                        name=["red","green","blue"][color],line=dict(color=["red","green","blue"][color])) for color in range(3)]

    def plot(self, x):
        y = self.get_values(x)
        fig = go.Figure()
        for color in range(3):
            fig.add_trace(go.Scatter(x=x, y=[i[color] for i in y], mode='lines', 
                                        name=["red","green","blue"][color],line=dict(color=["red","green","blue"][color])))
        return fig

    def to_binary(self, rgb):
        return tuple([int(i*255) for i in rgb])

    def create_frames(self, x, size):
        frames = []
        rgb_values = self.get_values(x)
        for i, rgb in enumerate(rgb_values):
            rgb = self.to_binary(rgb)
            color = 'rgb' + str(rgb)
            frame = go.Frame(data=[go.Scatter(
                x=[0], y=[0],
                mode='markers',
                marker=dict(
                    color=color,
                    size=size,  # Adjust size to your preference
                    symbol='circle'  # Set marker shape to circle
                ))], name=str(i))
            frames.append(frame)
        return frames
    
    def create_frame2(self, x):
        rgb_values = self.get_values(x)
        frame = []
        for i, rgb in enumerate(rgb_values):
            rgb = self.to_binary(rgb)
            color = 'rgb' + str(rgb)
            frame.append(go.Scatter(
                    x=[0], y=[0.5],
                    mode='markers',
                    marker=dict(
                        color=color,
                        size=250,  # Adjust size to your preference
                        symbol='circle'  # Set marker shape to circle
                    )))
        return frame

    def animate(self, x, fps=30,size=250):
        frames = self.create_frames(x, size)
        # Create layout
        layout = go.Layout(
            title='Color Changing Circle Animation',
            xaxis=dict(range=[-1, 1]),
            yaxis=dict(range=[-1, 1]),
            hovermode=False
        )
        # Create figure
        fig = go.Figure(
            data=[go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='rgb(0, 0, 0)', size=size, symbol='circle'))],  # Initial color
            frames=frames,
            layout=layout
        )
        # Add buttons for animation control
        fig.update_layout(updatemenus=[dict(type='buttons',
                                            showactive=False,
                                            buttons=[dict(label='Play',
                                                        method='animate',
                                                        args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)])])])

        return fig

    def show(self, x):
        fig = make_subplots(rows=1,cols=2)
        lines = self.lines(x)
        anim_fig = self.animate(x)
        fig.add_trace(lines[0], row=1, col=1)
        fig.add_trace(lines[1], row=1, col=1)
        fig.add_trace(lines[2], row=1, col=1)
        fig.add_trace(go.Scatter(x=[0,0], y=[-1,2], mode='lines', line=dict(color='black')), row=1, col=1)
        fig.add_trace(go.Scatter(x=[0], y=[0.5], mode='markers', marker=dict(color='rgb(255, 0, 0)', size=250, symbol='circle')), row=1, col=2)
        sub_frame = self.create_frame2(x)
        frames =[go.Frame(data=[go.Scatter(visible=True),go.Scatter(visible=True),go.Scatter(visible=True),go.Scatter(x=[x[i],x[i]],visible=True),
                        anim],
                  traces=[0,1,2,3,4]) for i,anim in enumerate(sub_frame)]   # define 20 frames
        fig.frames = frames
        fig.update_layout(updatemenus=[dict(type='buttons',
                                            showactive=False,
                                            buttons=[dict(label='Play',
                                                        method='animate',
                                                        args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True)])])])
        fig.update_yaxes(range=[-0.1, 1.1]) 
        return fig
