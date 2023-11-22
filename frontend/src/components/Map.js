import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { themeStyles } from '../styles/themes/medievalFantasyTheme.css';
import { mapContainerId } from '../../sharedDependencies';

const Map = () => {
  const [currentPosition, setCurrentPosition] = useState({ lat: 51.505, lng: -0.09 });
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    // TODO: Fetch locations from the backend or a static file
    // setLocations(fetchedLocations);
  }, []);

  return (
    <div id={mapContainerId} style={themeStyles.map}>
      <MapContainer center={currentPosition} zoom={13} scrollWheelZoom={false} style={{ height: '100%', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        {locations.map((location, index) => (
          <Marker key={index} position={location.coordinates}>
            <Popup>
              {location.name}
              <br />
              {location.description}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
};

export default Map;