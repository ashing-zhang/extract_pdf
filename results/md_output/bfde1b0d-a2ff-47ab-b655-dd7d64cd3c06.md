Reverse Engineering the Raspberry Pi Camera V2: A study of
(cid:73)
Pixel Non-Uniformity using a Scanning Electron Microscope
R. Matthewsa,∗, M. Sorella, N. Falknerb
aThe University of Adelaide, School of Electrical and Electronic Engineering, Adelaide, SA, 5005 AUS.
bThe University of Adelaide, School of Computer Science, Adelaide, SA, 5005 AUS.
Abstract
9102 naJ 21  ]VI.ssee[  1v70830.1091:viXra
In this paper we reverse engineer the Sony IMX219PQ image sensor, otherwise known as
the Raspberry Pi Camera v2.0. We provide a visual reference for pixel non-uniformity by
analysing variations in transistor length, microlens optic system and in the photodiode. We
use these measurements to demonstrate irregularities at the microscopic level and link this
to the signal variation measured as pixel non-uniformity used for unique identification of
discrete image sensors.
Keywords:
1. Introduction
Sensor pattern noise (SPN) has been accepted as a viable method to identify a unique
camera responsible for taking a specific image. These methods rely on the non-uniform
nature of individual pixels, known as pixel non-uniformity (PNU), to establish a unique
reference pattern. There exists a gap in the literature which clearly explains the cause
of PNU especially with the purpose of instructing jurors in mind. Sensor pattern noise
(SPN) methods based on PNU are important for intelligence communities, law enforcement
communities and can have additional applications for photographers wishing to establish
ownership without relying on metadata or additional watermarks. While SPN methods are
(cid:73)
Copyright 2018. This manuscript version is made available under the CC-BY-NC-ND 4.0 license
http://creativecommons.org/licenses/by-nc-nd/4.0/
∗Corresponding author
Email address: richard.matthews@adelaide.edu.au (R. Matthews)
Preprint submitted to Digital Investigation January 15, 2019

accepted by the forensic community (an important Daubert criterion) there is a risk that
a lay juror with no mathematical background may be confused by the evidence presented
in a court setting. This can be confounded by issues such as the CSI effect where a juror
expects Hollywood science to replace real forensic methodology.
In this paper we explore some of the physical characteristics of the IMX219PQ image
sensor, providing direct evidence of variation which may cause SPN. We reverse engineer the
design, and analyse three features of an image sensor under a scanning electron microscope:
transfer gate length, variations within the microlens optic system (LOS) and variations
within the photodiode region. It is hypothesised that the variations within these features
are principally caused by tolerances in the manufacturing process, can visually be seen under
significant magnification and may cause PNU.
2. Related Work
The existing literature provides a blanket statement for the source of PNU [1]. “PNU
is caused by the inhomogeneity of silicon wafers and other imperfections during the man-
ufacturing process.” The focus of the literature since has been directed on improving the
method first identified as distinct from identifying the underlying source. A gap exists to
address this underlying assumption as to the source of PNU within the pixel unit of an
image sensor. Correcting this assumption provides greater clarity for forensic identification
purposes should the literature be challenged in a legal setting.
We focus on three feature categories which may cause the PNU used to uniquely identify
each sensor. These are variations within the length of the transfer gate, within the micro lens
optical system (LOS) and within the photo diode itself. The justification for this approach
is given in the related works below.
[2] provides an analysis of key geometric properties within the structures of an image
sensor and how this affects the charge transfer efficiency (CTE). Variable CTE values for
discrete pixels will cause PNU. The geometric aspects investigated by [2] include the pho-
todiode size, the transfer gate length and the sense node (SN) storage area. The SN is also
referred to as a floating diffusion (FD). The two terms are able to be used interchangeably.
2

In both cases, the region refers to a highly-conductive region without resistive connection
to allow the storage of charge, in effect a capacitor. [2] showed that in all instances of
geometric variation it was the length of these critical geometries which affected the CTE of
the device. Incomplete transfer between photodiode and SN also causes image lag and noise
on an individual pixel [3]. This provides justification to measure the lengths of the transfer
gate as well as the photo diode as a possible source of PNU.
Differences in the transfer gate are also responsible for dark current variations. Dark
current is generated in the transfer gate by the silicon to silicon dioxide interfaces or by
defects below the surface of the gate itself [3]. We have previously shown the use of dark
current for thermal identification of image sensors [4, 5]. Dark current has also been used
in isolation and in hybrid methods for image identification alongside PRNU [6]. Measuring
differences within the transfer gate thus provides additional motivation as larger gates will
provide greater surface area interactions for dark current generation.
We have previously shown the contamination of lens effects within the SPN methodology
[7, 8, 9]. In [10] the non-uniform output of a photodiode was presented. [10, Fig. 2 c] shows
the non-uniform output of the diode while being excited by a 7V laser through various inci-
dent angles. The output of the photodiode was measured to vary between 305mv and 208mv
depending on the incident angle of the laser. Given the non-uniform output demonstrated
in this work it is hypothesised that this could be a contributor to PNU in image sensors.
Assuming this is a contributor of PNU in image sensors, it is theorised that this would
manifest via misalignment within the micro LOS of a sensor focusing or filtering photons
to different areas of the depletion region of the photodiode. This would be distinctively
different to PNU being caused by variance in doping levels within the photodiode or the size
of the photodiode during manufacture. Such misalignments should be possible to visually
see under cross-sectional analysis through the use of a scanning electron microscope. This
provides justification to examine the micro LOS of the image sensor.
3

3. Research Methodology
Using a Sony IMX219PQ [11] image sensor as the test subject imaging was performed
under a FEI Dual Beam Helios Nano Lab 600 scanning electron microscope [12]. The
Helios allows imaging down to 1nm at 15kV. Minimal preparation of the sample is required
before imaging since the image sensor is made primarily of silicon and hence, is conductive
to the electron beam. The IMX219PQ comes as a package board from the Raspberry Pi
Foundation. The sensor is de-constructed to obtain the silicon wafer in isolation to the
peripheral circuit and attached to the FEI imaging platform by way of adhesive conductive
dot. The platform is tilted to 52 to enable imaging and machining by the gallium focused
ion beam. Under magnification, a layer of platinum was deposited above the area to be
excavated to prevent fracturing (Figure 1a). After the platinum is deposited a process of
staged cuts were made using a gallium ion beam to create an excavated area through the
sensor that can be imaged (Figure 1b). The gallium ion beam is capable of machining down
to 5nm allowing precise cuts to be made. This is a destructive process.
Using a magnification of up to 100,000x (400nm scale), a current of 0.086 - 0.17nA and
voltage of 5-15kV, images are then obtained of the top layers of the integrated CIS containing
the pinned photodiode and the associated supply and readout circuitry. Only the top silicon
wafer is studied.
4. Data Collection and Analysis
4.1. Reverse Engineering
Using [3], Figure 2 and 3 presents the layers of the CIS with each region identified.
The sensor is a back illuminated sensors (BIS) with a pinned photodiode (PPD). The P+
pinning layer can be seen in Figure 3. In Figure 2 the width of the sensor is measured as
approximately 6um. This is consistent with the provided literature from Sony [13] which also
indicates a dual wafer design. This is confirmed in these images with the bonding surface
between the two wafers indicated in Figure 2 at the appropriate distance from the top of the
micro LOS. In the micro LOS the structure can be seen as a main lens, passivation layer,
4

(a) (b)
Figure 1: (a) Platinum (shown here as a growth on top of the micro-array) is deposited on the CIS to prevent
micro-fractures forming during the excavation process. (b) The excavated region of the CIS is shown after
the Gallium ion beam has been used to step out the material present in the region of interest. Several passes
are used to obtain a smooth, polished cross-section.
Bayer filter and then a minor sub lens nestled in between the nodes of the wire grid. The
photodiode region is identified and isolated between two layers of P doped semiconductor
used to prevent cross talk. The isolation regions are located directly beneath the wire grid
used for optical isolation. This is seen clearer in Figure 3 where the microscope is focused
onto the read out circuit layer of the image sensor.
Using reference images from [3], the Bayer filter elements visible in Figure 3 are identified
as green and red. This is made out as the red filter elements are thinner than green with
the blue elements being thicker and filling almost the entire layer. The transfer nodes (TX)
are visible within the image. From here it is possible to identify the individual transfer, M1
reset (RST), M2 source follower (SF) and M3 column select transistors within the Metal 4
layer. The wiring for each of these nodes is then routed to the underlying metal layers to
provide read out access to the circuit, most likely on the peripheral or underlying silicon
wafer. The TX wires are seen within the Metal 2 layer while it is assumed that the Vcc,
5

Figure 2: A horizontal cross-section of the IMX219PQ sensor. Each region of the sensor is clearly identified.
select and column bus tracks are visible in Metal 1.
Using the information identified above in conjunction with [14] and [3] an equivalent
circuit can be identified for the Sony IMX219PQ BIS pixel unit. From examining [14] we
see that the sensor has the capability to store defective pixels in one of three modes: single
pixels, single adjacent pixels by Bayer element and individual blocks of 2x4 adjacent pixels.
Understanding how the sensor stores defects provides insight to the readout structure. It
follows that the sensor has a pixel unit comprising of 2x4 photodiodes sharing a single
readout circuit. Using [3] the pixel unit is comprised of a circuit of eleven transistors for
every eight photodiodes. Using the familiar nomenclature of average number of transistors
per pixel we see the IMX219PQ is a 1.375T (11 transistors per 8 pixels) design. This is
indicated in Figure 4.
We suspect that the clover leaf pattern is utilised as per previous Sony iterations, in
particular the sensor (Sony IMX145) in [3]. Unlike the equivalent circuit shown in [3, Fig.
9] we show only two sense node locations corresponding to the sense node in each of the two
pixel subgroups noting the work of Fontaine in [3, Fig. 10] showing these two locations in
6

Figure 3: A secondary cross-section of the IMX219PQ sensor. The structure of the photodiode and circuit
is identified within the image.
the centre of the clover leaf. We note that the charge for each photodiode when read out
will be distributed on both of these nodes in parallel due to Kirchoff’s Current Law. The
readout circuitry is an important distinction to clarify as it forms a significant source of dark
current. Sensors that demonstrate a different readout structure (3T, 4T, 2T, 1.75T) provide
a possible source of difference for forensic identification. The dark current of such sensor
configurations should be measured in future work. The clover leaf pattern should also be
confirmed by imaging the bottom of the sensor.
7

Figure 4: The equivalent circuit for the IMX219PQ pixel unit. Inset shows the scanning direction for read
out of the IMX219PQ sensor when identifying a 2x4 pixel defect on the sensor taken from [14].
4.2. Transfer Gate
Measurements were taken of the readout node of the photo diode using the SEM built
in measurement tool. These were then verified manually by printing images to scale and
measuring by hand. These results are shown in Table 1.
(a) (b) (c)
Figure 5: The length of six transfer gates are taken across three separate pixel units Odd gates are green,
even gates are red. (a) Transfer gates 1 and 2. (b) Transfer gates 3 and 4. (c) Transfer gates 5 and 6.
There is variation with all transfer nodes measured. The mean of all six transfer nodes is
8

Table 1: Transfer Gate Length
Pixel SEM Measure (nm) Manual Measure (nm) Average (nm)
1 305 308 307
2 322 329 326
3 370 370 370
4 363 364 364
5 379 380 380
6 366 378 372
353nm. Measuring the variance to the mean from each transfer node we obtain a double sided
tolerance of +27nm and -46nm. Extrapolating, this leads to a feature size of 350nm with an
engineering tolerance of +/-50nm. The polysilicon layer has an average thickness of 160nm
with metal 4 being approximately 280nm in thickness. This is consistent with the 130nm
lithography process design rules in [15] noting we have labelled our metal layers in reverse
order. This measurement is not consistent throughout the layer with the layer increasing
and decreasing in thickness throughout the images obtained. This thickness variation will
cause minor geometric changes to the features of the circuit. These thickness variations will
become more pronounced in top layers as the variations stack.
4.3. Micro Lens Optical System
Two Green-Red Bayer elements are overlaid in Figure 6. In 6a the microimagery is pre-
sented for the two immediate, same colour, neighbouring elements with noticeable variations
in the structure of these two identical Bayer elements. The stained blue shows a large seg-
ment missing to the right where as the stained yellow is slightly thicker. The cropped images
are run through a Canny edge detector in FIJI [16] to provide a binary gate to compare the
two filter elements against. This result of the Canny edge detector is presented in 6b. White
is where element 1, previously tinted yellow, is presented. Dark grey is element 2 previously
tinted blue. Dark white is where both elements are, and light grey is where only element 1 is
present. This shows the contrasting differences between the two CFA elements with a hole
9

in element 2 positioned above the optical block (metal grid). These minor variations are
likely to create optical aberrations known as Seidel aberrations affecting where individual
photons will strike the depletion region of the photodiode [17, 18].
(a) (b)
Figure 6: (a) Overlay of the two Green-Red Bayer filter elements. (b) The overlay of the two Green-Red
Bayer filter elements as a binary image using FIJI [16].
The Bayer filter is not the only region that is observed to have irregularities which will
cause optical aberrations. Sectioning off the top layer of the micro LOS provides access to
the passivation layer in between the micro lens and the Bayer elements. Shown in Figure
7 holes in the passivation layer are visible directly above the wire grid elements. This is
another defect within the structure of the sensor that is not uniformly distributed on every
pixel. Once again, the formation of holes within the upper layers of the micro LOS are likely
to cause aberrations [17, 18].
4.4. Photodiode Variations
Four photodiodes and their length are shown in Figure 8. We note the presence of a
charging artefact due to the highly conductive metal layers causing a smearing effect into
the photodiode region on the image. Measurements are taken well away from this artefact
to avoid any contamination. Measurements are taken from the SEM and then confirmed
via manual scaling as per section 4.2. These measurements are displayed in Table 2. All
measurements show variation from photodiode to photodiode.
The mean photodiode length is measured as 894nm with a variance of +/-14nm. The
nominal pixel length is stated as being 1120nm (1.12um) [14]. Measuring the length of the
10

Figure 7: Sectioning the top lens layer of the IC reveals the passivate later above the Bayer elements below
the micro lenses. Bubbles are evident above the wire grid in random locations on the surface of the chip.
Table 2: Photodiode length
Photodiode SEM Measure (nm) Manual Measure (nm) Average (nm)
1 Gr 910 899 905
2 R 890 873 882
3 Gr 880 879 880
4 R 910 905 908
isolation in between the photodiode regions we can obtain a measurement for the average
pixel length. The P dielectric isolation is manually measured as above and displayed in
Table 3. A mean measurement is obtained as 240nm. Adding the two mean measurments
11

Figure 8: Four photodiodes from two separate pixel units compared for length.
together obtains an average pixel length of 1134nm (1.13um). The four pixels in Figure 8
are manually measured to obtained a length of 451nm. This provides a mean measurement
of 1127.5nm (1.13um). These measurements indicate that the pixel length is slightly larger
than stated in the documentation due to manufacturing tolerance.
The variance in sizes across pixels are likely to be a significant cause of PNU on the sensor
as different sized photodiodes will measure different amounts of light and have different
amounts of dark current.
5. Discussion
Dark current and Photo Response Non-Uniformity noise are leading candidates in SPN
methods for identification of discrete image sensors from a candidate photo. [6] and [1] are
12

Table 3: Isolation Length
P Isolation Manual Measure (nm)
1 Gr 232
2 R 234
3 Gr 264
4 R 228
both indications of how this method can be used with great success. The defects shown
in Sections 4.2 and 4.4 are the features within the image sensor and the electrical circuit
which are likely candidates to cause the non-uniform characteristics of both Dark Current
and Photo Response non-uniformity used for unique identification.
Lens aberrations are known to link images to cameras [19]. Shown in Section 4.3 are
irregularities in the micro LOS that is inseparable from the image sensor. Lens aberrations
normally link an image to a LOS that is able to be separated from a camera. In the case
presented here, the defects within the micro LOS are inseparable from the sensor itself and
as such should provide a forensic link to the image sensor as opposed to a LOS.
It is important to note that when we and the literature have referred to manufacturing
defects we are not referring quality control issues in the typical sense. Where defects would
normally cause the scrap of the sensor or entire wafer, the defects we discuss are minimal
and still allow the sensor to operate within the designed engineering tolerance. It is this
variability within tolerance that is being exploited here for forensic identification. While
this trace is treated as unique it is also important to note that this has not been proven.
The largest scale test of this method has been done by [20] where it was found, using the
current state-of-the-art method, PCE identification has a false acceptance rate of less than
3 in 125,000. As this work has been conducted with the juror in mind, it is important to
highlight this distinction for the purposes of the Daubert criterion.
13

6. Conclusion and Future Work
In this paper we have demonstrated pixel non-uniformity within the silicon structure of
the image sensor at the microscopic level. We have demonstrated discontinuities between
discrete layers within the image sensor. While these discontinuities do not affect the overall
image performance capabilities of the sensor they do contribute to a layer of additive noise
known as PNU. Particular attention has been paid to the transfer gates and the associated
read out circuitry. This work has drawn attention to the variability of physical character-
istics of the electronic circuits on an imaging sensor to visualise how sensor pattern noise
may, at least in part, be explained. We have not considered the variation in semiconductor
performance due to chemical-level variability such as doping concentration and contamina-
tion, nor have other read-out circuitry configurations been analysed, which are matters for
future study. Our exploration of the physical dimensional variability may also be useful in
explaining, in part, the origins of sensor pattern noise to a lay audience
7. Acknowledgements
This research did not receive any specific grant from funding agencies in the public, com-
mercial, or not-for-profit sectors. This work was supported with supercomputing resources
provided by the Phoenix HPC service at the University of Adelaide. The authors acknowl-
edge the facilities, the scientific and technical assistance, of the Australian Microscopy and
Microanalysis Research Facility at Adelaide Microscopy, the University of Adelaide. This re-
search is supported by an Australian Government Research Training Program (RTP) Schol-
arship and forms part of a thesis chapter.
References
[1] J. Lukas, J. Fridrich, M. Goljan, Digital camera identification from sensor pattern noise, IEEE Trans-
actions on Information Forensics and Security 1 (2) (2006) 205–214.
[2] S. Rizzolo, V. Goiffon, M. Estribeau, O. Marcelot, P. Martin-Gonthier, P. Magnan, Influence of pixel
design on charge transfer performances in cmos image sensors, IEEE Transactions on Electron Devices
65 (3) (2018) 1048–1055. doi:10.1109/TED.2018.2790443.
14

[3] E. R. Fossum, D. B. Hondongwa, A review of the pinned photodiode for ccd and cmos image sensors,
IEEE Journal of the Electron Devices Society 2 (3) (2014) 33–43. doi:10.1109/JEDS.2014.2306412.
[4] R. Matthews, M. Sorell, N. Falkner, Thermal effects of dark current on blind source camera identifi-
cation, in: Proceedings of the 4th Interdisciplinary Cyber Research Workshop, Tallinn University of
Technology, Tallinn, Estonia, 2018, pp. 37–41.
[5] R. Matthews, M. Sorell, N. Falkner, Determining image sensor temperature using dark current, arXiv
preprint arXiv:1901.02113, “unpublished”.
[6] K. Kurosawa, K. Kuroki, K. Tsuchiya, N. Igarashi, N. Akiba, Case studies and further improvements
on source camera identification, in: Proc.SPIE, Vol. 8665, 2013, pp. 8665 – 8665 – 14. doi:10.1117/
12.2003311.
[7] R. Matthews, M. Sorell, N. Falkner, Isolating lens aberrations within fixed pattern noise, in: Proceed-
ings of the 3rd Interdisciplinary Cyber Research Workshop, Tallinn University of Technology, Tallinn,
Estonia, 2017, pp. 21–24.
[8] R. Matthews, M. Sorell, N. Falkner, Isolating lens aberrations within fixed pattern noise using photo
response non-uniformity noise, in: 24th International Symposium of the Australian and New Zealand
Forensic Science Society, Australian New Zealand Forensic Science Society, Perth, Australia, 2018, p. 1.
[9] R. Matthews, M. Sorell, N. Falkner, An analysis of optical contributions to a photo-sensor’s ballistic
fingerprints, arXiv preprint arXiv:1808.08684, “unpublished”.
[10] A. Chandrakanta, H. Devassy, The non-uniform characteristics of a photodiode, International Advanced
Research Journal in Science, Engineering and Technology.
[11] J. Sony Semiconductor, IMX219PQ data sheet, https://www.sony-semicon.co.jp/products en/new
pro/april 2014/imx219 e.html, accessed 7/01/2019.
[12] FEI, Helios nanolab 450 / 450 s / 450 ml / 650 / 600i user operation manual v51, https://mc2.engin.
umich.edu/wp-content/uploads/sites/227/2015/11/Helios.pdf, accessed 7/01/2019.
[13] J. Sony Semiconductor, IMX219PQH5 Module Design Reference Manual v2.2, https:
//github.com/rellimmot/Sony-IMX219-Raspberry-Pi-V2-CMOS/blob/master/IMX219PQH5
Module Design Reference Manual ver2.2 140425.pdf, accessed 7/01/2019.
[14] J. Sony Semiconductor, IMX219PQH5-C data sheet, https://github.com/rellimmot/Sony-IMX219-
Raspberry-Pi-V2-CMOS/blob/master/RASPBERRY%20PI%20CAMERA%20V2%20DATASHEET%
20IMX219PQH5 7.0.0 Datasheet XXX.PDF, accessed 7/01/2019.
[15] S. Tyagi, M. Alavi, R. Bigwood, T. Bramblett, J. Brandenburg, W. Chen, B. Crew, M. Hussein,
P. Jacob, C. Kenyon, C. Lo, B. McIntyre, Z. ma, P. Moon, P. Nguyen, L. Rumaner, R. Schweinfurth,
S. Sivakumar, M. Stettler, M. Bohr, A 130 nm generation logic technology featuring 70 nm transistors,
dual vt transistors and 6 layers of cu interconnects, in: Technical Digest - International Electron Devices
15

Meeting, 2000, pp. 567 – 570. doi:10.1109/IEDM.2000.904383.
[16] J. Schindelin, I. Arganda-Carreras, E. Frise, V. Kaynig, M. Longair, T. Pietzsch, S. Preibisch, C. Rue-
den, S. Saalfeld, B. Schmid, et al., Fiji: an open-source platform for biological-image analysis, Nature
methods 9 (7) (2012) 676. doi:10.1038/nmeth.2019.
¨
[17] P. L. V. Seidel, Uber den Einfluss der Theorie der Fehler, mit welchen die durch Optische Instrumente
gesehenen Bilder behaftet sind, und u¨ber die mathematischen Bedingungen ihrer Authebung, Abhand-
lungen der naturwissenschaftlich-technischen Commission der Bayerischen Akademie der Wissenschafte,
1857.
[18] F. A. Jenkins, H. E. White, Fundamentals of optics, Tata McGraw-Hill Education, 1957.
[19] K. San Choi, E. Y. Lam, K. K. Wong, Source camera identification using footprints from lens aberration,
Digital Photography II 6069 (2006) 60690J. doi:10.1117/12.649775.
[20] M. Goljan, J. Fridrich, T. Filler, Large scale test of sensor fingerprint camera identification, in: Media
Forensics and Security, Vol. 7254, International Society for Optics and Photonics, 2009, p. 72540I.
16