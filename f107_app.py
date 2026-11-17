import math
import streamlit as st

st.set_page_config(page_title='F10.7 Interactive Calculator', layout='wide')
st.title('Three flavours of F10.7 solar radio flux')
st.caption('Interactive demonstration of atmospheric, Earth–Sun distance, and URSI scale corrections')

flux = st.slider('Measured solar flux (sfu)', 60, 300, 150, 5)
elevation = st.slider('Solar elevation (degrees)', 10, 90, 30, 5)
distance = st.slider('Earth–Sun distance (AU)', 0.983, 1.017, 1.000, 0.001, format='%.3f')

atmloss = 0.9875 + 0.0115 / math.sin(math.radians(elevation))
observed = flux * atmloss
adjusted = observed * distance**2
ursi = 0.9 * adjusted

st.divider()
a, b, c = st.columns(3)
a.metric('Observed F10.7', f'{observed:.2f} sfu')
b.metric('Adjusted F10.7', f'{adjusted:.2f} sfu')
c.metric('URSI Series-D', f'{ursi:.2f} sfu')
st.info(f'Atmospheric correction factor: {atmloss:.5f} ({(atmloss - 1) * 100:.2f}% correction)')
st.latex(r'F_{\mathrm{obs}}=F_{\mathrm{meas}}\left(0.9875+0.0115\csc h\right)')
st.latex(r'F_{\mathrm{adj}}=F_{\mathrm{obs}}(r/1\,\mathrm{AU})^2')
st.latex(r'F_{\mathrm{URSI}}=0.9F_{\mathrm{adj}}')
st.caption('Educational calculator based on the supplied formulas; it is not an official data product.')
